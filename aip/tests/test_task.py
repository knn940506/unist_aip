import unittest

from aip.builder.base import *


class TaskTest(unittest.TestCase):
    """
    test object task works
    """

    def test_object(self):
        print("start obect")

        objects = [
            {"name":"rooma"},
            {"name":"roomb"},
            {"name":"ball1"},
            {"name":"ball2"},
            {"name":"ball3"},
            {"name":"ball4"},
            {"name":"left"},
            {"name":"right"},
        ]
        answer = "(:objects rooma roomb ball1 ball2 ball3 ball4 left right)"

        parser = Object(objects)
        self.assertEqual(parser.pddl, answer)

    def test_predicate_task(self):
        print("start predicate")

        predicates = [
            {"name":"ROOM","args":["x"]},
            {"name":"BALL","args":["x"]},
            {"name":"GRIPPER","args":["x"]},
            {"name":"at-robby","args":["x"]},
            {"name":"at-ball","args":["x", "y"]},
            {"name":"free","args":["x"]},
            {"name":"carry","args":["x", "y"]}
        ]
        answer = "(:predicates (ROOM ?x) (BALL ?x) (GRIPPER ?x) (at-robby ?x) (at-ball ?x ?y) (free ?x) (carry ?x ?y))"

        task = Predicate(predicates)
        self.assertEqual(task.pddl, answer)

    def test_initial_state_task(self):
        print("start state")

        states = [
            {"name":"ROOM","args":["rooma"]},
            {"name":"ROOM","args":["roomb"]},
            {"name":"BALL","args":["ball1"]},
            {"name":"BALL","args":["ball2"]},
            {"name":"BALL","args":["ball3"]},
            {"name":"BALL","args":["ball4"]},
            {"name":"at-ball","args":["ball1", "rooma"]}
        ]
        answer = "(:init (ROOM rooma) (ROOM roomb) (BALL ball1) (BALL ball2) (BALL ball3) (BALL ball4) (at-ball ball1 rooma))"

        task = State(states)
        self.assertEqual(task.pddl, answer)

    def test_goal_task(self):
        """
        at-ball(ball1, roomb), ..., at-ball(ball4, roomb) must be true.
        Everything else we don’t care about.
        """
        print("start goal")

        goals = [
            {"name":"at-ball","args":["ball1", "roomb"],"option":"and"},
            {"name":"at-ball","args":["ball2", "roomb"],"option":"and"},
            {"name":"at-ball","args":["ball3", "roomb"],"option":"and"},
            {"name":"at-ball","args":["ball4", "roomb"],"option":"and"},
        ]

        answer = "(:goal (and (at-ball ball1 roomb) (at-ball ball2 roomb) (at-ball ball3 roomb) (at-ball ball4 roomb)))"

        task = Goal(goals)
        self.assertEqual(task.pddl, answer)


    def test_action_task(self):
        """
        Precondition: ROOM(x), ROOM(y) and at-robby(x) are true.
        Effect: at-robby(y) becomes true. at-robby(x) becomes false.
        Everything else doesn’t change.

        (:action move :parameters (?x ?y)
        :precondition (and (ROOM ?x) (ROOM ?y)
        (at-robby ?x))
        :effect (and (at-robby ?y)
        (not (at-robby ?x))))
        """

        print("start Action")
        answer = "(:action move :parameters (?x ?y) :precondition (and (ROOM ?x) (ROOM ?y)) :effect (and (at-robby ?y) (not (at-robby ?x))))"

        action_kwargs = {
            "name": "move",
            "args": ["x", "y"],
            "precondition": [
                {"name": "ROOM", "args": ["x"], "option": "and"},
                {"name": "ROOM", "args": ["y"], "option": "and"},
            ],
            "effect": [
                {"name": "at-robby", "args": ["y"], "option": "and"},
                {"name": "at-robby", "args": ["x"], "option": "and", "flag":"not"},
            ]
        }

        task = Action(**action_kwargs)
        self.assertEqual(task.pddl, answer)

if __name__ == "__main__":
    unittest.main()

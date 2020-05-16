(define (domain test)
	:predicates (ROOM ?x) (BALL ?x) (GRIPPER ?x) (at-robby ?x) (at-ball ?x ?y) (free ?x) (carry ?x ?y)
	(:action move :parameters (?x ?y) :precondition (and (ROOM ?x) (ROOM ?y)) :effect (and (at-robby ?y) (not (at_robby ?x))))
	(:action pick_up :parameters (?x ?y ?z) :precondition (and (BALL ?x) (ROOM ?y) (GRIPPER ?z) (at_robby ?y)) :effect (and (carry ?z ?x) (not (at_ball ?x ?y)) (not (free ?z))))
	(:action drop :parameters (?x ?y ?z) :precondition (and (BALL ?x) (ROOM ?y) (GRIPPER ?z) (carry ?z ?x) (at_robby ?y)) :effect (and (at_ball ?x ?y) (free ?z) (not (carry ?z ?x))))
)
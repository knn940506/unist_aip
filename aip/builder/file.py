import pathlib
import os
import json

from aip.builder.base import *
    

#http://csci431.artifice.cc/notes/pddl.html

class FileBuilder:
    def __init__(self, name, save_dir, import_dir):
        self.name = name
        self.save_dir = save_dir
        self.import_dir = import_dir

    def export(self):
        path = os.path.join(self.save_dir, f"{self.name}.pddl")

        with open(path, "w") as f:
            f.write(self.content)

    def load_json(self, path):
        with open(path) as fp:
            data = json.load(fp)

        return data

    @property
    def content(self):
        raise NotImplementedError()

class DomainFile(FileBuilder):

    symbol = "domain"

    def __init__(self, name, save_dir, import_dir):
        super().__init__(name, save_dir, import_dir)

        self.predicate = None
        self.actions = []

        self.read_predicate()
        self.read_actions()
        
    def read_predicate(self):
        predicates = self.load_json(os.path.join(self.import_dir, 'predicates.json'))
        self.predicate = Predicate(predicates)

    def read_actions(self):
        actions = self.load_json(os.path.join(self.import_dir, 'actions.json'))

        for name, spec in actions.items():
            self.actions.append(Action(**spec))

    @property
    def content(self):
        """ predicates + actions
        (define (domain <domain name>)
            <PDDL code for predicates>
            <PDDL code for first action>
            [...]
            <PDDL code for last action>
        )
        """

        parts = [
            f"(define (domain {self.name})",
            self.predicate.pddl_component,
            ]
        parts.extend([x.pddl for x in self.actions])
        
        content = "\n\t".join(parts)
        content += "\n)"
        return content

class ProblemFile(FileBuilder):

    symbol = 'problem'

    def __init__(self, name, save_dir, import_dir, problem_data):
        super().__init__(name, save_dir, import_dir)

        self.domain_name = name
        self.name = name + "_problem"
        self.data = problem_data

        self.object = None
        self.state = None
        self.goal = None

        self.read_objects()
        self.read_state()
        self.read_goal()

    def read_objects(self):
        """
        Driver, Customers, Stores(S1, S2, S3, Juice, Sauce)
        """
        objects = self.load_json(os.path.join(self.import_dir, 'objects.json'))
        for customer in self.data.keys():
            objects.append({'name': customer})

        self.object = Object(objects)

    def read_state(self):
        """
        Customer / Store / Food

            - Set customers, stores, foods
            - Set food locations to store
        """

        states = []
        for customer in self.data.keys():
            states.append({"name":"CUSTOMER","args":[customer]})

        stores = self.load_json(os.path.join(self.import_dir, 'stores.json'))
        stores = [s['name'] for s in stores]
        for store in stores:
            states.append({"name":"STORE", "args":[store]})

        foods = self.load_json(os.path.join(self.import_dir, 'stores.json'))
        foods = [s['menu'] for s in foods]
        for food in foods:
            states.append({"name":"FOOD", "args":[food]})

        sells = self.load_json(os.path.join(self.import_dir, 'stores.json'))
        sells = [list(s.values()) for s in sells]
        for sell in sells:
            states.append({"name":"sell", "args":sell})

        self.state = State(states)

    def read_goal(self):
        """
        - Dirver
            - All capacity = 0
        - Customer
            - All order delivered   
        """

        goals = []
        for customer, item in self.data.items():
            for order in item['orders']:
                goals.append({
                    "name":"delivered",
                    "args":[customer, order['menu'], str(order['qty'])],
                    "option":"and"
                    })

        self.goal = Goal(goals)

    @property
    def content(self):
        """ objects + initial-states + goals
        (define (problem <problem name>)
            (:domain <domain name>)
            <PDDL code for objects>
            <PDDL code for initial state>
            <PDDL code for goal specification>
        )
        """

        parts = [
            f"(define (problem {self.name})",
            f"(:domain {self.domain_name})",
            self.object.pddl,
            self.state.pddl,
            self.goal.pddl,
            ]
        
        content = "\n\t".join(parts)
        content += "\n)"
        return content

class PddlBuilder(FileBuilder):
    def __init__(self, raw_data, save_dir, import_dir):
        req_id, problem_data = self.process_data(raw_data)

        super().__init__(req_id, save_dir, import_dir)
        self.domain = DomainFile(req_id, save_dir, import_dir)
        self.problem = ProblemFile(req_id, save_dir, import_dir, problem_data)

    def process_data(self, raw_data):
        return raw_data['req_id'], raw_data['requests']

    def export(self):
        self.domain.export()
        self.problem.export()

    @property
    def content(self):
        return "PddlFildBuilder"
    
if __name__ == "__main__":
    save_dir = pathlib.Path().absolute()
    import_dir = os.path.join(save_dir, 'predefined')

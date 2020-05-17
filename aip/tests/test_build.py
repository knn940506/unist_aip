import unittest
import pathlib
import os
import json

from aip.builder.file import *

class BuildTest(unittest.TestCase):
    """
    test object task works
    """

    def test_domain(self):
        print("start domain")

        base_dir = pathlib.Path().absolute()
        save_dir = os.path.join(base_dir, 'results')
        import_dir = os.path.join(base_dir, 'predefined')

        builder = DomainFile("fromDomainBuilder", save_dir, import_dir)
        builder.export()

    def test_problem(self):
        print("start problem")

        base_dir = pathlib.Path().absolute()
        save_dir = os.path.join(base_dir, 'results')
        import_dir = os.path.join(base_dir, 'predefined')

        with open(os.path.join(base_dir, 'inputs', 'example_build_input.json')) as fp:
            test_data = json.load(fp)['requests']

        builder = ProblemFile("fromProblemBuilder", save_dir, import_dir, test_data)
        builder.export()

    def test_builder(self):
        print("start builder")

        base_dir = pathlib.Path().absolute()
        save_dir = os.path.join(base_dir, 'results')
        import_dir = os.path.join(base_dir, 'predefined')
        
        with open(os.path.join(base_dir, 'inputs', 'example_build_input.json')) as fp:
            test_data = json.load(fp)

        builder = PddlBuilder(test_data, save_dir, import_dir)
        builder.export()

if __name__ == "__main__":
    unittest.main()

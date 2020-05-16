import unittest
import pathlib
import os

from aip.builder.file import *

class BuildTest(unittest.TestCase):
    """
    test object task works
    """

    def test_domain(self):
        print("start domain")

        req_id = "test"
        save_dir = pathlib.Path().absolute()
        import_dir = os.path.join(save_dir, 'predefined')

        builder = DomainFile(req_id, save_dir, import_dir)
        builder.export()

    def test_problem(self):
        print("start problem")

        req_id = "test"
        save_dir = pathlib.Path().absolute()
        import_dir = os.path.join(save_dir, 'predefined')

        builder = ProblemFile(req_id, save_dir, import_dir, {})
        builder.export()

    def test_builder(self):
        print("start builder")

        raw_data = {"req_id": "test"}
        save_dir = pathlib.Path().absolute()
        import_dir = os.path.join(save_dir, 'predefined')

        builder = PddlBuilder(raw_data, save_dir, import_dir)
        builder.export()

if __name__ == "__main__":
    unittest.main()

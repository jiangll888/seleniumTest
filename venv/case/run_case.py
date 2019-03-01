import unittest
import os

class RunCase(unittest.TestCase):
    def test_case(self):
        suite = unittest.defaultTestLoader.discover(os.getcwd(),"unittest_case*.py")
        unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    # r = RunCase()
    # r.test_case()
    unittest.main()


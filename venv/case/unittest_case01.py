import unittest

class Test(unittest.TestCase):
    def test_01(self):
        print("this is test01")

    def test_02(self):
        print("this is test02")

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test("test_01"))
    suite.addTest(Test("test_02"))
    unittest.TextTestRunner().run(suite)

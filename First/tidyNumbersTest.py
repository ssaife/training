import unittest
from tidyNumbers import FileTester, TidyNumberGenerator


def broken_function():
    raise Exception('This is broken')


class MyTestCase(unittest.TestCase):
    def testFileNotExist(self):
        with self.assertRaises(Exception):
            FileTester.testFile("hi")

    def testFileInputs(self):
        with self.assertRaises(Exception):
            FileTester.testfile("mytest.txt")

    def testNegative(self):
        with self.assertRaises(Exception):
            TidyNumberGenerator.findTidyNum("-9")

    def testInvalidInput(self):
        with self.assertRaises(Exception):
            TidyNumberGenerator.findTidyNum("99#9")
            TidyNumberGenerator.findTidyNum("aaa")
            TidyNumberGenerator.findTidyNum("9aa")
            TidyNumberGenerator.findTidyNum("9 8")

    def testOutput(self):
        self.assertEqual(TidyNumberGenerator.findTidyNum("14235"), "13999")


if __name__ == '__main__':
    unittest.main()

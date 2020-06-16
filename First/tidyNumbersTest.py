import unittest
from tidyNumbers import testfile
from tidyNumbers import findTidyNum


class MyTestCase(unittest.TestCase):
    def test_file_not_exist(self):
        # make sure that the file exception is handled
        self.assertEqual(testfile("tryThis.txt"), ['File Not Found'])

    def test_string_negative_null(self):
        self.assertEqual(testfile("mytest.txt"),
                         ['8999', 'Negative Numbers Not Accepted', 'Invalid Input', 'Invalid Input', '44'])


if __name__ == '__main__':
    unittest.main()

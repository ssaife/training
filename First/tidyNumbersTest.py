import unittest
from tidyNumbers import testfile
from tidyNumbers import findTidyNum


class MyTestCase(unittest.TestCase):
    def test_file(self):
        # make sure that the file exception is handled
        self.assertEqual(testfile("tryThis.txt"), ['File Not Found'])


if __name__ == '__main__':
    unittest.main()

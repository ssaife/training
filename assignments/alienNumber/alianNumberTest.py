import unittest
from alianNumber import AlianNumberTranslator, FileTester


class MyTestCase(unittest.TestCase):
    def testAlianNumberTranslator(self):
        self.assertEqual(AlianNumberTranslator('1011', '01', '0123456789').translate(), '11')
        self.assertEqual(AlianNumberTranslator('foo', 'of8', '0123456789').translate(), '9')
        self.assertEqual(AlianNumberTranslator('foo', 'of8', 'of8').translate(), 'foo')
        self.assertEqual(AlianNumberTranslator('ff', '0123456789abcdef', '01').translate(), '11111111')

    def testInvalidInputException(self):
        with self.assertRaises(Exception):
            AlianNumberTranslator(22, '235', '123').translate()
        with self.assertRaises(Exception):
            AlianNumberTranslator('22', 12, '123').translate()
        with self.assertRaises(Exception):
            AlianNumberTranslator('22', '235', 123).translate()

    def testDuplicateException(self):
        with self.assertRaises(Exception):
            AlianNumberTranslator('22', '1223', '123').translate()
        with self.assertRaises(Exception):
            AlianNumberTranslator('2', '123', '1233').translate()

    def testInputFile(self):
        FileTester('A-large-practice.in').test_File()
        FileTester('A-small-practice.in').test_File()
        with self.assertRaises(Exception):
            FileTester('123').test_File()


if __name__ == '__main__':
    unittest.main()

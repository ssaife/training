import unittest
from alianNumber import AlianNumberTranslator, FileTester


class MyTestCase(unittest.TestCase):
    def testAlianNumberTranslator(self):
        self.assertEqual(AlianNumberTranslator.translateAlianNumber('1011', '01', '0123456789'), '11')
        self.assertEqual(AlianNumberTranslator.translateAlianNumber('foo', 'of8', '0123456789'), '9')
        self.assertEqual(AlianNumberTranslator.translateAlianNumber('foo', 'of8', 'of8'), 'foo')
        self.assertEqual(AlianNumberTranslator.translateAlianNumber('ff', '0123456789abcdef', '01'), '11111111')

    def testInvalidInputException(self):
        with self.assertRaises(Exception):
            AlianNumberTranslator.translateAlianNumber(22, '235', '123')
        with self.assertRaises(Exception):
            AlianNumberTranslator.translateAlianNumber('22', 12, '123')
        with self.assertRaises(Exception):
            AlianNumberTranslator.translateAlianNumber('22', '235', 123)

    def testDuplicateException(self):
        with self.assertRaises(Exception):
            AlianNumberTranslator.translateAlianNumber('22', '1223', '123')
        with self.assertRaises(Exception):
            AlianNumberTranslator.translateAlianNumber('2', '123', '1233')

    def testInputFile(self):
        FileTester.testFile('A-large-practice.in')
        FileTester.testFile('A-small-practice.in')


if __name__ == '__main__':
    unittest.main()

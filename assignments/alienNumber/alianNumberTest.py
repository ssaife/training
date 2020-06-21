import unittest
from alianNumber import AlianNumberTranslator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(AlianNumberTranslator.translateAlianNumber('f', '0f8', '0123456789'), '1')


if __name__ == '__main__':
    unittest.main()
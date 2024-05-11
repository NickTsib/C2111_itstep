import unittest
from para8_4 import *


class My_Test(unittest.TestCase):

    def test_arg(self):
        self.assertEqual(adder(2, 2), 4)


if __name__ == '__main__':
    unittest.main()

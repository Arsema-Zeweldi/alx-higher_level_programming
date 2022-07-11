#!/usr/bin/python3
"""unittest cases for square.py"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """cases to be evaluated"""
    def test_init(self):
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_init_2(self):
        self.assertRaises(TypeError, Square)

if __name__ == '__main__':
    unittest.main()

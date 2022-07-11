#!/usr/bin/pyhton3
"""unittest cases for rectangle.py"""


import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """cases to be evaluated"""
    def test_init(self):
        r1 = Rectangle(5, 8)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        r2 = Rectangle(2, 5)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)

if __name__ == '__main__':
    unittest.main()

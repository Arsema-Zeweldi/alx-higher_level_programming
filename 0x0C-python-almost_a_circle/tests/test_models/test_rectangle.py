#!/usr/bin/pyhton3
"""unittest cases for rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """cases to be evaluated"""

    def test_initialization(self):
        """Tests Rectangle with 2 values"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        """Tests Rectangle with 3 values"""
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)
        """Tests Rectangle with 4 values"""
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, Rectangle._Base__nb_objects)
        """Tests Rectangle with width as string value"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        """Tests Rectangle with height as string value"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        """Tests Rectangle with x as string value"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        """Tests Rectangle with y as string value"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        """Tests Rectangle with width as negative value"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        """Tests Rectangle with height as string value"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        """Tests Rectangle with width as zero value"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        """Tests Rectangle with height as zero value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        """Tests Rectangle with x as negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        """Tests Rectangle with y as negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()

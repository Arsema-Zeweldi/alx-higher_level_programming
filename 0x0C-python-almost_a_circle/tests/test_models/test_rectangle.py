#!/usr/bin/pyhton3
"""unittest cases for rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """cases to be evaluated"""

    def test_rec_2(self):
        """Tests Rectangle with 2 values"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)

    def test_rec_3(self):
        """Tests Rectangle with 3 values"""
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)

    def test_rec_4(self):
        """Tests Rectangle with 4 values"""
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.id, Rectangle._Base__nb_objects)

    def test_rec_5(self):
        """Tests Rectangle with width as string value"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rec_6(self):
        """Tests Rectangle with height as string value"""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rec_7(self):
        """Tests Rectangle with x as string value"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rec_8(self):
        """Tests Rectangle with y as string value"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rec_9(self):
        """Tests Rectangle with width as negative value"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rec_10(self):
        """Tests Rectangle with height as string value"""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rec_11(self):
        """Tests Rectangle with width as zero value"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rec_12(self):
        """Tests Rectangle with height as zero value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rec_13(self):
        """Tests Rectangle with x as negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rec_14(self):
        """Tests Rectangle with y as negative"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()

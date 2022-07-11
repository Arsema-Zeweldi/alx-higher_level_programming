#!/usr/bin/python3
"""unittest cases for base.py"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """cases to be evaluated"""
    def test_init(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id(self):
        base = Base(100)
        self.asserEqual(base.id, 100)

    def test_json(self):
        pass

if __name__ == '__main__':
    unittest.main()

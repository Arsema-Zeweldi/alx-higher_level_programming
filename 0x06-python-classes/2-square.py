#!/usr/bin/python3
"""The Square class defines a square"""


class Square:
    """Private instance attribute"""
    def __init__(self, size=0):
        if type(size) != int:
            raise ValueError("size must be >= 0")
        elif size < 0:
            raise TypeError("size must be an integer")

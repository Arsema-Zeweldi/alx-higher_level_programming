#!/usr/bin/python3
"""The Rectangle class defines a rectangle"""


class Rectangle:
    """Private instance attributes - height and width"""
    def __init__(self, width=0, height=0):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @height.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an iinteger")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (int(self.__height) * int(self.__width))

    def perimeter(self):
        return ((int(self.__height) * 2) + (int(self.__width) * 2))

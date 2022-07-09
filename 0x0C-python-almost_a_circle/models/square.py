#!/usr/bin/python3
"""Inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """super class"""
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__height = size
        self.__width = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: int):
        self.__size = value
        self.width = self.height = value
        

    def __str__(self):
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, size))

    def update(self, *args, **kwargs):
        expect = ['id', 'size', 'x', 'y']
        if args:
            for a, b in zip(attr, args):
                setattr(self, a, b)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {
                'id': id, 'x': x, 'size': size, 'y': y}

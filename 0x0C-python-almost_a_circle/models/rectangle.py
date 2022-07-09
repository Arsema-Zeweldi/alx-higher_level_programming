#!/usr/bin/python3
"""Inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def check_x_and_y(self, name: str, value: object, c=False):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if c:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.check_x_and_y('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.check_x_and_y('y', y, True)
        self.__y = y

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle with #"""
        print('\n'*self.__y, end='')
        for c in range(self.__height):
            print(' ' * self.x + '#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                    args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        return {
                'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

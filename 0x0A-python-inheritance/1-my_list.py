#!/usr/bin/python3
""" The MyList class inherits list"""


class MyList(list):
    """public instance method"""
    def print_sorted(self):
        """sorted list"""
        new_list = (sorted(self))
        print(new_list)

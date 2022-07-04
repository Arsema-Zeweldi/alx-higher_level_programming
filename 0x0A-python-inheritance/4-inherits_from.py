#!/usr/bin/python3
"""returns true or false"""


def inherits_from(obj, a_class):
    """inheritance"""
    return type(obj) != a_class and issubclass(type(obj), a_class)

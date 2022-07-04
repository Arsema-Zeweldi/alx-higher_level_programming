#!/usr/bin/python3
"""returns true or false"""


def is_same_class(obj, a_class):
    """no self"""
    return a_class == type(obj)

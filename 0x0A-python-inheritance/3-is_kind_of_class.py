#!/usr/bin/python3
"""returns true or false"""


def is_kind_of_class(obj, a_class):
    """is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

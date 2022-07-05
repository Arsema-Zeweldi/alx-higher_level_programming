#!/usr/bin/python3
"""Returns the dict descr. for JSON serialization"""


def class_to_json(obj):
    """ obj dict"""
    return obj.__dict__

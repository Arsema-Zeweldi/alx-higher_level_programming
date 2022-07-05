#!/usr/bin/python3
"""Returns the JSON representation of an object"""


def to_json_string(my_obj):
    """my object"""
    import json
    return json.dumps(my_obj)

#!/usr/bin/python3
"""Writes an object to a text file using a JSON repr"""


def save_to_json_file(my_obj, filename):
    """filename, my_obj"""
    with open(filename, mode='w', encoding="utf-8") as MyFile:
        import json
        new = json.dumps(my_obj)
        return (MyFile.write(new))

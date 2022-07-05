#!/usr/bin/python3
"""Creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """filename"""
    with open(filename) as MyFile:
        return json.loads(MyFile.read())

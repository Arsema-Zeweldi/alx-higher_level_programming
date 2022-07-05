#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """filename, text"""
    with open(filename, mode='w', encoding="utf-8") as MyFile:
        return (MyFile.write(text))

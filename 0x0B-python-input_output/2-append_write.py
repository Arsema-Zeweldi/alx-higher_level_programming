#!/usr/bin/python3
"""Appends a string to a text file"""


def append_write(filename="", text=""):
    """filename, text"""
    with open(filename, mode='a', encoding="utf-8") as MyFile:
        return (MyFile.write(text))

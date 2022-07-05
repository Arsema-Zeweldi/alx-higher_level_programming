#!/usr/bin/python3
"""Reads a text"""


def read_file(filename=""):
    """filename"""
    with open(filename, mode='r', encoding="utf-8") as MyFile:
        for line in MyFile:
            print(line, end='')

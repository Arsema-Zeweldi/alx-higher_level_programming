#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """list of list"""
    if n <= 0:
        return []
    pas_tri = [[1]]
    for c in range(2, n+1):
        new = [0] + pas_tri[c-2] + [0]
        pas_tri.append([sum(par) for par in zip(new, new[1:])])
    return pas_tri

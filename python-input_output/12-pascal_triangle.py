#!/usr/bin/python3
"""
This module will print a triangle
"""


def pascal_triangle(n):
    """
    print Pascal's triangle of n
    """
    result = []
    for i in range(1, n + 1):
        row = []
        C = 1
        for j in range(1, i + 1):
            row.append(C)
            C = C * (i - j) // j
        result.append(row)
    return result

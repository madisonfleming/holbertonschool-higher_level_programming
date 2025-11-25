#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type annotated function to return sum of float arguments in list"""
    sum: float = 0.0
    for i in input_list:
        sum = sum + i
    return sum

#!/usr/bin/env python3
from typing import List
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """type annotated function to return sum of float and int arguments in list"""
    sum: float = 0.0
    for i in mxd_lst:
        sum = sum + i
    return sum

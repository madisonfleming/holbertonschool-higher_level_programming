#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type annotated function to return a function that multiplies a float"""
    def multi(my_float: float) -> float:
        return my_float * multiplier
    return multi

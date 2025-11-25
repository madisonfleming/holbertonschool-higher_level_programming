#!/usr/bin/env python3
from typing import List
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """type annotated function to return a tuple"""
    return k, v * v

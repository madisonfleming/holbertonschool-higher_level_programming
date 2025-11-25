#!/usr/bin/env python3
from typing import List
import typing


def element_length(lst: typing.Iterable[
        typing.Sequence]) -> List[typing.Tuple[typing.Sequence, int]]:
    """annotated function to return appropriate types"""

    return [(i, len(i)) for i in lst]

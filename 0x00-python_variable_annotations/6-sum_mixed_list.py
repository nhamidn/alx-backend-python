#!/usr/bin/env python3
"""sum_mixed_list Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of a list of integers and floats."""
    result: float = 0.0
    for i in mxd_lst:
        result = result + i
    return result

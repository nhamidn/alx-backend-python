#!/usr/bin/env python3
"""sum_list Module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """calculate sum of input_list."""
    result: float = 0.0
    for i in input_list:
        result = result + i
    return result

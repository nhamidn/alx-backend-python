#!/usr/bin/env python3
"""sum_list Module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """calculate floor of float number."""
    result: float = 0.0
    for i in input_list:
        result = result + i
    return result

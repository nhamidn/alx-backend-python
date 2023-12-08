#!/usr/bin/env python3
"""make_multiplier Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Create and return a multiplication function."""
    def mult(x: float) -> float:
        return x * multiplier
    return mult

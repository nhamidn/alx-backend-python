#!/usr/bin/env python3
"""to_kv Module"""
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with the string k and the square of the int/float v."""
    return k, v ** 2

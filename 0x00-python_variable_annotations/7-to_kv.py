#!/usr/bin/env python3
"""to_kv Module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with the k and the square of v."""
    return str(k), float(v ** 2)

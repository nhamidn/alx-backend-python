#!/usr/bin/env python3
"""make_multiplier Module"""
from typing import Iterable, Sequence, List, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length of each element."""
    return [(i, len(i)) for i in lst]

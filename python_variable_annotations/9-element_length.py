#!/usr/bin/env python3
"""annotate I guess"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """this should work"""
    return [(i, len(i)) for i in lst]

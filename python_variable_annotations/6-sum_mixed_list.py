#!/usr/bin/env python3
"""This is a comment for learning mixed types"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """add a mixed list together"""
    total: float = 0
    for number in mxd_list:
        total += number
    return total

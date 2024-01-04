#!/usr/bin/env python3
"""This is a comment for learning mixed types"""


def sum_mixed_list(mxd_list: int | float) -> float:
    """add a mixed list together"""
    total: float = 0
    for number in mxd_list:
        total += number
    return total

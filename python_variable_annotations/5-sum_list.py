#!/usr/bin/env python3
"""A list of floats returns the sum of them all"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This is a function that adds a list together"""
    total: float = 0
    for number in input_list:
        total += number
    return total

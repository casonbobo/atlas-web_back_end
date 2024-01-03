#!/usr/bin/env python3
"""A list of floats returns the sum of them all"""


def sum_list(input_list: list[float]) -> float:
    """This is a function that adds a list"""
    total: int = 0
    for number in input_list:
        total += number
    return total

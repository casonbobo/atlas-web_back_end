#!/usr/bin/env python3
"""To multiply"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """To make multiply"""
    def multiply(num: float) -> float:
        return multiplier * num
    return multiply

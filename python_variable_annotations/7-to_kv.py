#!/usr/bin/env python3
"""This takes a str and a num to make a tup"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This is a toople"""
    kv_tuple: Tuple = (k, v*v)
    return kv_tuple
 
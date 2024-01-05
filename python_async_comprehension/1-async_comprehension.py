#!/usr/bin/env python3
"""This set of tasks is pissing me off"""
import asyncio
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """This returns a list of randomized
        numbers collected from the previous task"""
    return [i async for i in async_generator()]

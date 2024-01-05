#!/usr/bin/env python3
"""Learning Async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This is a comment"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

#!/usr/bin/env python3
"""This set of tasks is pissing me off"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """I forgot this comment"""
    start_time = time.time()
    runs = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*runs)
    end_time = time.time()
    return end_time - start_time

#!/usr/bin/env python3
"""learning concurrent"""
wait_random = __import__("0-basic_async_syntax").wait_random
import asyncio


async def wait_n(n: int, max_delay: int):
    """Will this work MrAtlas"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    output = await asyncio.gather(*tasks)
    return output

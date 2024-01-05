#!/usr/bin/env python3
"""learning concurrent"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Will this work MrAtlas"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    output = await asyncio.gather(*tasks)
    return sorted(output)

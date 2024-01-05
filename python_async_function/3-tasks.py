#!/usr/bin/env python3
"""This does tasks I guess"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """I am honestly not sure what this is supposed to do"""
    task = asyncio.create_task(wait_random(max_delay))
    return task

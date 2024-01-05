#!/usr/bin/env python3
"""This does tasks I guess"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10):
    """I am honestly not sure what this is supposed to do"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task

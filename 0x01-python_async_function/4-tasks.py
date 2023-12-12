#!/usr/bin/env python3
"""4-tasks module."""
import asyncio
from typing import List
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function."""
    delays = []
    tasks = []

    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: delays.append(x.result()))
        tasks.append(task)

    for task in tasks:
        await task
    return delays

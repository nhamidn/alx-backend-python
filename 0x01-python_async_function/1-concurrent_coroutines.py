#!/usr/bin/env python3
"""concurrent_coroutines module."""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function."""
    delays = []
    tasks = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda x: delays.append(x.result()))
        tasks.append(task)

    for task in tasks:
        await task
    return delays

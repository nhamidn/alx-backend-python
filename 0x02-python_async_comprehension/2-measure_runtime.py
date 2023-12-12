#!/usr/bin/env python3
"""measure_runtime module."""

import asyncio
import timeit
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that executes function 4 times in parallel."""

    start = timeit.default_timer()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    stop = timeit.default_timer()
    return stop - start

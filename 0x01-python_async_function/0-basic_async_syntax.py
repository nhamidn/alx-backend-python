#!/usr/bin/env python3
"""basic_async_syntax module."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random function."""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand

#!/usr/bin/env python3
"""async_comprehension module."""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async_comprehension coroutine."""
    values = [i async for i in async_generator()]
    return values

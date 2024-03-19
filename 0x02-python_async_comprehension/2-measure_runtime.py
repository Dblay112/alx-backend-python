#!/usr/bin/env python3
"""imported modules below"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """a measure_runtime coroutine that will execute
    async_comprehension
    four times in parallel using asyncio.gather"""
    start_t = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_t

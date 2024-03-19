#!/usr/bin/env python3
"""imported modules below"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator to yields 10 random numbers between 0 and 10,
    waiting 1 second"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

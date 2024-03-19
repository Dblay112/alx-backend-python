#!/usr/bin/env python3
"""imported modules below"""
import asyncio
import random


async def async_generator():
    """Async generator to yields 10 random numbers between 0 and 10,
    waiting 1 second"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

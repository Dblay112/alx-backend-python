#!/usr/bin/env python3
"""imported modules below"""
from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async coroutine that uses async comprehension
    to collect 10 random numbers"""
    return [_ async for _ in async_generator()]

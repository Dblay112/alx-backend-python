#!/usr/bin/env python3
"""import modules below"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """
    Waits for a random delay between 0 and max_delay
    seconds

    Args:
    max_delay(int): maximum delay in seconds

    Returns:
    float: actual delay returned in seconds
    """
    delay_time = random.random() *  max_delay
    await asyncio.sleep(delay_time)
    return delay_time

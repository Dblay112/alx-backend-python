#!/usr/bin/env python3
"""imported module
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


# Define the task_wait_random function
def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asyncio.task using asncio.create_task"""
    return asyncio.create_task(wait_random(max_delay))

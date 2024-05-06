#!/usr/bin/env python3
"""
Async routine that spawns wait_random n times with the specified max_delay
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns the
    list of delays.
    """
    return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

#!/usr/bin/env python3
"""
Async routine that spawns wait_random n times with the specified max_delay
"""
import asyncio
from typing import List

from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times.
    """
    wait_times = await asyncio.gather(*(wait_random(max_delay)
                                        for _ in range(n)))
    return sorted(wait_times)

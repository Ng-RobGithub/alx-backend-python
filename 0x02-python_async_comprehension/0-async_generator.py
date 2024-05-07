#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This coroutine loops 10 times, asynchronously waiting for 1 second
    on each iteration, then yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

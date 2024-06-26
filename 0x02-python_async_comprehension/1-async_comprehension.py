#!/usr/bin/env python3
""" a coroutine called async_comprehension that takes no arguments"""

from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using async comprehension over async_generator.

    This coroutine uses async comprehension to collect 10 random numbers
    generated by the async_generator coroutine. It waits for each random
    number to be generated asynchronously.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [i async for i in async_generator()]

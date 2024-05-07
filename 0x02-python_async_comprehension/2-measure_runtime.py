#!/usr/bin/env python3
""" coroutine that will measure the total runtime and return it"""

import asyncio
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing async_comprehension four times in
    parallel.

    This coroutine executes async_comprehension four times in parallel
    using asyncio.gather(). It measures the total runtime for all four
    executions and returns it.

    Returns:
        float: The total runtime for executing async_comprehension four times
        in parallel.
    """
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()

    return end_time - start_time

#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n
"""
import asyncio
from typing import List
from random import uniform

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple instances of task_wait_random concurrently."""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]


if __name__ == "__main__":
    import asyncio

    async def main():
        n = 5
        max_delay = 6
        print(await task_wait_n(n, max_delay))

    asyncio.run(main())

import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait randomly from 0 to `max_delay` seconds."""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_random(n: int = 10) -> None:
    """Wait randomly `n` times."""
    await asyncio.gather(*(wait_random() for _ in range(n)))


async def main() -> None:
    """Run the main function."""
    await task_wait_random()


if __name__ == "__main__":
    asyncio.run(main())

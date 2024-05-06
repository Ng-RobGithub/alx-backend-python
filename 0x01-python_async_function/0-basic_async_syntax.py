import asyncio
import random


@asyncio.coroutine
def wait_random(max_delay=10):
    """
    Coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    yield asyncio.sleep(delay)
    yield delay


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(wait_random()))
    print(loop.run_until_complete(wait_random(5)))
    print(loop.run_until_complete(wait_random(15)))
    loop.close()

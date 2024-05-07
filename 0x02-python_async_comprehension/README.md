0x02. Python - Async Comprehension

Async comprehensions are a feature introduced in Python 3.6 that allow you to create asynchronous generators and comprehensions in a concise and expressive way.
Background:
In Python, comprehensions are concise syntax for creating collections such as lists, dictionaries, and sets from existing iterables.
Syntax:
The syntax for async comprehensions is similar to regular comprehensions, but with the async keyword before the expression:

python
Copy code
async def async_generator():
    async for item in async_iterable:
        yield item

async_comp = [async_expr async for async_item in async_iterable]
-------------------------------------------------------------------------------------------
How to Write an Asynchronous Generator:
An asynchronous generator is a coroutine that produces values asynchronously. To define an asynchronous generator, you use the async def syntax followed by the yield statement within an asynchronous iteration construct (such as async for).

Here's an example of how to write an asynchronous generator:

python
Copy code
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate an asynchronous operation
        yield i
----------------------------------------------------------------------------------------
How to Use Async Comprehensions:
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate an asynchronous operation
        yield i

async def main():
    async_comp = [i async for i in async_generator()]
    print(async_comp)

asyncio.run(main())
----------------------------------------------------------------------------
How to Type-Annotate Generators:
To type-annotate generators, you can use the Generator type from the typing module.
from typing import Generator

def my_generator(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i
-----------------------------------------------------------------------------------------
Tasks:
0. Async Generator
mandatory
Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
1. Async Comprehensions
mandatory
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.
2. Run time for four parallel comprehensions
mandatory
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

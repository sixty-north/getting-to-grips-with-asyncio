import asyncio

from coop.main import (search, lucas, is_prime)


async def thirteen_digit_prime(x):
    return (await is_prime(x)) and len(str(x)) == 13


async def monitor_future(future, interval_seconds):
    while not future.done():
        print("Waiting...")
        await asyncio.sleep(interval_seconds)
    print("Done!")


loop = asyncio.get_event_loop()

search_task = asyncio.ensure_future(
    search(lucas(), thirteen_digit_prime),
    loop=loop)

monitor_task = asyncio.ensure_future(
    monitor_future(search_task, 1.0),
    loop=loop)

search_and_monitor_future = asyncio.gather(
    search_task, monitor_task)

loop.run_until_complete(search_and_monitor_future)
print(search_task.result())
loop.close()


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
future = loop.create_future()

coro_obj = search(lucas(),
                  thirteen_digit_prime)

search_task = loop.create_task(coro_obj)

loop.create_task(monitor_future(search_task, 1.0))
loop.run_until_complete(search_task)
print(search_task.result())
loop.close()


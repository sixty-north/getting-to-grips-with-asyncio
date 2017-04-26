import asyncio

from coop.main import (search, lucas, is_prime)


async def thirteen_digit_prime(x):
    return (await is_prime(x)) and len(str(x)) == 13


async def monitored_search(iterable, predicate, future):
    try:
        found_item = await search(iterable, predicate)
    except ValueError as not_found:
        future.set_exception(not_found)
    else:  # no exception
        future.set_result(found_item)

async def monitor_future(future, interval_seconds):
    while not future.done():
        print("Waiting...")
        await asyncio.sleep(interval_seconds)
    print("Done!")


loop = asyncio.get_event_loop()
future = loop.create_future()

coro_obj = monitored_search(lucas(),
                            thirteen_digit_prime,
                            future)

loop.create_task(coro_obj)

loop.create_task(monitor_future(future, 1.0))
loop.run_until_complete(future)
print(future.result())
loop.close()


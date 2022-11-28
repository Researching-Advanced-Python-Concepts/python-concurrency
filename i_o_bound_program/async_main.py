# cooperative multitasking

import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as res:
        print(f"Read {res.content_length} from {url}")


async def download_all_sites(sites):
    # session can be shared across all tasks because they are all
    # running on the same thread
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            # creates a list of task also takes care of starting them
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        # keeps the session context alive until all of the tasks have
        # completed
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://cython.org",
    ] * 80
    start_time = time.time()
    # starting of the event loop and tell it which tasks to run
    # asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    # instead of get_event_loop().run_until_complete we can run
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    # Downloaded 160 in 1.5841059684753418 seconds
    # thread version took 8.194037199020386 seconds 
    # synchronous version took 23.108558654785156 seconds


# scales far better than threading
# each task takes far fewer resources and less time to create than a
# thread, so creating and running more of them works well
# runs super fast

# if a task doesn't hand control back to the event loop, it(EL) can't break it
# proper placement of async and await, requests doesn't notify the event loop
# that it is blocked
# a minor mistake in code can cause a task to run off and hold the processor for
# a long time, starving other tasks that need running
# threading requires extra effor

import concurrent.futures
import requests
import threading
import time

# even though this obj seems global its specific to each
# individual thread hence thread-safe
# the object takes care of separating accesses from diff.
# threads to diff. data
thread_local = threading.local()


def get_session():
    # for the 1st time each thread will create a single session its called
    # then it will use that session for subsequent call throughout its lifetime
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    # each thread creates its own Session
    session = get_session()
    with session.get(url) as res:
        print(f"Read {len(res.context)} from {url}")


def download_all_sites(sites):
    # create a pool of threads each of which can run concurrently (at the same time)
    # executor controls how and when each of the threads in the pool will run.
    # it will execute the request in the pool.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # runs the passed in function on each of the sites in the list
        # it runs it automatically in concurrent way using the pool of threads
        # it is managing
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://cython.org",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    # Downloaded 160 in 8.194037199020386 seconds
    # synchronous version took 23.108558654785156 seconds

# It uses multiple threads to have multiple open requests out to website
# at the same time, allowing our program to overlap the waiting times and
# get the final result faster.

# more code required
# make decision beforehand to which data is shared betn threads
# threads can interact in ways that are hard to detect and somewhat track
# race conditions are possible which gives unpredictability to our code
# this also means debugging is difficult
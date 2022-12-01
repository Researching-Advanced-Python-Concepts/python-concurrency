# takes full advantage of the multiple CPUs

import requests
import multiprocessing
import time


session = None


def set_global_session():
    # making it global so that for each process will have its own
    # session
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(response.content)} from {url}")


def download_all_sites(sites):
    # pool creates a number of separate python interpreter processes
    # and has each one run the specified function on some of the items
    # in the iterable
    # if not provided the number of processes to create in the Pool,
    # multiprocessing.Pool will determine the no. of CPUs in our computer
    # and match that
    # each process in our Pool has its own memory space. So they can't share
    # things like Session object.
    # we want to create one session for each process (not everytime the fn is
    # called) and this is made possible by initializer
    # there is no way to pass a return value back from the initializer to the fn
    # called by download_site() so we intialize a global session that is unique
    # for each process as they have their own memory space
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://cython.org",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    # Downloaded 160 in 7.185908317565918 seconds
    # async version took 1.5841059684753418 seconds
    # thread version took 8.194037199020386 seconds 
    # synchronous version took 23.108558654785156 seconds

# relatively easy to setup and requires little extra code
# take full advantage of the CPU power in our computer

# it requires some extra setup and the global session obj is strange
# we have to spend some time thinking about which variables will be
# accessed in each process
# can't see gains in I/O bound problems
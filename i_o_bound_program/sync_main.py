import requests
import time


def download_site(url, session):
    with session.get(url) as res:
        print(f"Read {len(res.content)} from {url}")


def download_all_sites(sites):
    # session allows connection pooling so we can use the
    # previous connection which will make it faster
    # we can also reuse the cookies, headers, auth, etc
    with requests.Session() as session:
        for url in sites:
            download_site(url, session=session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "https://cython.org",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
    # Downloaded 160 in 23.108558654785156 seconds

# This type of programs are quite good if it takes only 2 seconds
# and we rarely run it
# it's simple, easy to debug and we can predict what happens next

# it's a different case if it takes hours and we need to run it
# frequently

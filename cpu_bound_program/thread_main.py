import concurrent.futures
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sum(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sum(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    # Duration 4.929476499557495 seconds
    # sync version takes 4.920512676239014 seconds

# we can see it takes some more time as it spends time creating
# or setting up threads

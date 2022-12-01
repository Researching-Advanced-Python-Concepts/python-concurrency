# designed to share heavy CPU workloads across multiple CPUs
# and this is where multiprocessing really shines


import multiprocessing
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers=numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    # Duration 1.5160069465637207 seconds
    # sync version takes 4.920512676239014 seconds
    # thread version takes 4.929476499557495 seconds
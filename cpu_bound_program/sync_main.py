import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    # Duration 4.920512676239014 seconds

# unlike I/O bound process the results are fairly consistent
# async and threading won't do much but rather slow the process down
# because as we know they utilize the time the cpu became idle to include
# and do other tasks rather then just doing sequentially
# so tearing and creating of threads and stuff will slow things down
# threads and asyncio(tasks) run on the same CPU in the same process
# so the CPU is doing all of the work of the non-concurrent code plus the
# extra code of setting up threads or tasks.

# in CPU bound problem there is no waiting and CPU is working as hard as
# it is allowed to work

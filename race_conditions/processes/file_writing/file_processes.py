# this doesn't result in a race condition on linux
# but better safe than sorry so use locks

from multiprocessing import Process
from multiprocessing import Lock
import os


def task(filename, arg):
    # task for writing data to a file
    # write data to the file
    for i in range(10000):
        # open the file
        with open(filename, "a") as file:
            # write one line
            print(f"Data line {i} from task {arg}.", file=file)


def task_with_lock(filename, arg, lock):
    # task for writing data to a file
    # write data to the file
    for i in range(10000):
        # acquire the lock
        with lock:
            # open the file
            with open(filename, "a") as file:
                # write one line
                print(f"Data line {i} from task {arg}.", file=file)


# protect the entry point
if __name__ == "__main__":
    # shared filename
    filename = "tmp.txt"
    lock = Lock()
    # delete the file if it exists
    try:
        os.remove(filename)
    except:  # noqa
        pass
    # start some processes to write to the same file
    # processes = [Process(target=task, args=(filename, i)) for i in range(50)]
    processes = [Process(target=task, args=(filename, i, lock))
                 for i in range(50)]
    # start the processes
    for process in processes:
        process.start()
    # wait for the processes to complete
    for process in processes:
        process.join()
    # read the file and report results
    with open(filename, "r") as file:
        # read entire file
        data = file.read()
        # split into lines
        data = data.strip().split("\n")
        # report total lines
        print(f"{filename} has {len(data)} lines")

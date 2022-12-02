# the thread calling the wait for will block until notified and
# the callable passed in as an argument returns a True value

# the thread is notified many times by diff. threads but will only
# unblock and continue execution once the condition in the callable
# is met
from time import sleep
from random import random
from threading import Thread
from threading import Condition


# target function
def task(thread_no, condition, work_list):
    print(f"Entered task for thread {thread_no}")
    # acquire the condition
    with condition:
        # block for a momemnt
        print(f"Entered for condition thread {thread_no}")
        value = random()
        sleep(value)
        # add work to the list
        # mutex within the condition ensure no race condition occur
        # hence thread-safe
        print(f"Working inside condition thread {thread_no}")
        work_list.append(value)
        print(f"Thread {thread_no} added {value}")
        # notify the waiting thread
        condition.notify()


# create a condition
condition = Condition()

# define work list
work_list = list()

# start a bunch of threads that will add work to the list
for i in range(5):
    worker = Thread(target=task, args=(i, condition, work_list))
    worker.start()

# wait for all threads to add their work to the list
with condition:
    # wait to be notified
    print("Waiting for the end")
    condition.wait_for(lambda : len(work_list) == 5)
    print(f"Done, got: {work_list}")

# first the 5 threads are started and each will acquire the condition
# and generate a random value and add to the shared list and notify
# the main thread

# the main thread waits on the condition and is notified each time
# one of the new thread finished but does not actually continue on
# and print a message until the condition of the lambda fn is True
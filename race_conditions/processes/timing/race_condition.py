# to force the race condition, we'll add a delay betn
# the new process starting and waiting on the condition.

# this will cause the new process to always miss the notification
# from the main process and wait forever
from time import sleep
from multiprocessing import Process
from multiprocessing import Condition


def task(condition):
    # process waiting to be notified
    # the fn sleep for a fraction of a second to force the timing
    # race condition, then acquire the condition and wait to be
    # notified
    # insert a dealy
    sleep(1)
    # wait to be notified
    print("Process: Waiting to be  notified...", flush=True)
    with condition:
        condition.wait()
    print("Process: Notified", flush=True)


# protect the entry point
if __name__ == "__main__":
    # create the shared condition variable
    condition = Condition()
    # create the new process
    process = Process(target=task, args=(condition,))
    # start the new process
    process.start()
    # allow the new process to start up, but not start waiting
    sleep(0.5)
    # notify the new process
    print("Main: Notifying the process")
    with condition:
        condition.notify()
    # wait for the task to complete
    process.join()
    print("Main: Done")


# the child process wakes up , acquires the condition and waits to be
# notified. Because the notification has already been sent, it is
# missed and the child process waits forever

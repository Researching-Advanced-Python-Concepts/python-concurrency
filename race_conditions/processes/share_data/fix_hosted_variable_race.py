# 1. multiprocessing.Lock
from time import sleep
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from multiprocessing import Lock


class SafeCounter:
    # custom counter class that encourages the os to context switch
    # in the middle of the operations, essentially forcing a
    # race condition
    def __init__(self, count):
        self._value = count

    # retrieve the variable
    def get(self):
        return self._value

    # add one to the variable
    def increment(self):
        # copy value
        tmp = self._value
        # allow a context switch
        sleep(0)
        # increment the value
        tmp = tmp + 1
        # allow a context switch
        sleep(0)
        # copy the updated value
        self._value = tmp

    # subtract one from the variable
    def decrement(self):
        # copy value
        tmp = self._value
        # allow a context switch
        sleep(0)
        # increment the value
        tmp = tmp - 1
        # allow a context switch
        sleep(0)
        # copy the updated value
        self._value = tmp


# custom manager to support custom classes
class CustomManager(BaseManager):
    # nothing
    pass


# task executed in a child process
def adder_task(counter, lock):
    for i in range(1000):
        with lock:
            counter.increment()


# task executed in a child process
def subtractor_task(counter, lock):
    for i in range(1000):
        with lock:
            counter.decrement()


# protect the entry point
if __name__ == "__main__":
    # register the custom class on the custom manager
    # so it knows how to make it
    CustomManager.register("SafeCounter", SafeCounter)
    lock = Lock()

    # create manager
    with CustomManager() as manager:
        # create the counter on the manager server process
        # and return proxy obj that can be shared with the child
        # processes and used to interact with the hosted object
        counter = manager.UnsafeCounter(0)
        # create child processes
        adder_process = Process(target=adder_task,
                                args=(counter, lock))
        subtractor_process = Process(target=subtractor_task,
                                     args=(counter, lock))
        # start child processes
        adder_process.start()
        subtractor_process.start()
        # wait for processes to complete
        adder_process.join()
        subtractor_process.join()
        # report the value
        print(f"Value: {counter.get()}")

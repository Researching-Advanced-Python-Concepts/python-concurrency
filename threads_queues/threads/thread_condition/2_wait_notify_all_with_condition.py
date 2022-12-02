from time import sleep
from random import random
from threading import Thread
from threading import Condition


# target function
def task(condition, number):
    # wait to be notified
    print(f"Thread {number} waiting...")
    with condition:
        # the thread acquire the condition and
        # block waiting to be notified
        condition.wait()
    # block for a moment
    value = random()
    sleep(value)
    # report a result
    print(f"Thread {number} got {value}")


# create a condition
condition = Condition()
# start a bunch of threads that will wait to be notified
for i in range(5):
    # ******** must wait before notifying ******
    worker = Thread(target=task, args=(condition, i))
    worker.start()

# block for a moment
sleep(1)
# notify all waiting threads that they can run
with condition:
    # wait to be notified
    condition.notify_all()
print("Line 35 on main thread")
# block until all non-daemon threads finish...
# when the main thread notified all 5 waiting threads. they wake up
# acquire the lock in the condition one at a time, perform their
# processing and then report their result

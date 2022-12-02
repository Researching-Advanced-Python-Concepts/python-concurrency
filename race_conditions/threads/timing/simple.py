# threads can also suffer race condition due to a bug with timing

# while using threading.Condition we must acquire the condition
# b4 we can call wait or notify, then release it once we're done
# this is done using the context manager

# ----------------------
# for the behaviour to work as intented, the notification from the
# 2nd thread must be sent after the 1st thread has started waiting
# if the order changes then the 1st thread will wait forever
# so ****wait b4 getting notified****
# this happens when the context is switched by the os that allows
# the 2nd thread to run b4 the 1st(this one waits)
from time import sleep
from random import random
from threading import Thread
from threading import Condition


def task(condition, data):
    # target function
    # block for a moment
    value = random()
    print(f"Inside task {value}")
    sleep(value)
    # wait for data
    with condition:
        print(".thread waiting on condition")
        condition.wait()
    print(f"Thread got data: {data}")


# create the condition
condition = Condition()

# create the data storage
data = list()
# create a new thread
thread = Thread(target=task, args=(condition, data))

# start the new thread
thread.start()

# block for a moment
value = random()
print(f"In main thread {value}")
sleep(value)
# acquire the condition
with condition:
    # store data
    data.append("We did it!")
    # notify waiting threads
    print("Main is notifying")
    condition.notify()

# if the main thread block finishes first then there is race condition
# as the main thread notifies even b4 the new thread waits for it
# this can happen sometimes and sometimes it will work just fine

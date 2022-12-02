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
    while True:
        # condition is inside the loop becuz we can release it each
        # iteration of the loop allowing main thread to acquire it
        with condition:
            print(".thread waiting on condition")
            # check the data
            if len(data) > 0:
                break
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
# treating the shared condition as a mutex lock
with condition:
    # store data
    data.append("We did it!")
    # notify waiting threads
    print("Main is notifying")
    condition.notify()

# both the main thread and new thread must acquire the condition b4
# interacting with the datalist (only one thread can acquire the
# condition at a time)

# new thread no longer waits on the condition but instead waits on the global
# state directly

# not so good as it consumes many CPU cycles doing essentially the same
# redundant check of the data list

# we can fix a race condition with a shared variable by protecting
# the shared variable with a mutex lock

# program is fixed if the result is 0
from time import sleep
from threading import Thread, Lock


# define a lock to protect the shared variable
lock = Lock()

# define the global variable
value = 0


# make additions into the global variable
def adder(amount, repeats, lock):
    global value
    for _ in range(repeats):
        with lock:
            # copy the value
            tmp = value
            # suggest a context switch to the os
            sleep(0)
            # change the copy
            tmp = tmp + amount
            # suggest a context switch to the os
            sleep(0)
            # copy the value back
            value = tmp


# make subtractions from the global variable
def subtractor(amount, repeats, lock):
    global value
    for _ in range(repeats):
        # lock.acquire()
        with lock:
            # copy the value
            tmp = value
            # suggest a context switch to the os
            sleep(0)
            # change the copy
            tmp = tmp - amount
            # suggest a context switch to the os
            sleep(0)
            # copy the value back
            value = tmp
        # lock.release()


# start a thread making additions
adder_thread = Thread(target=adder, args=(100, 1000000, lock))
adder_thread.start()

# start a thread making subtractions
subtractor_thread = Thread(target=subtractor, args=(100, 1000000, lock))
subtractor_thread.start()

# wait for both threads to finish
print('Waiting for threads to finish...')
adder_thread.join()
subtractor_thread.join()

# report the value
print(f'Value: {value}')
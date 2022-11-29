import threading
import time


x = 8192

lock = threading.Lock()


def double():
    global x, lock
    # tries to acquire the lock if its free
    # if its not free we're just waiting here
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum")
    lock.release()


def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

# this basically act like a synchronous program
# as only one thread has access to a resource at the time

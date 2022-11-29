import threading
import time

# A bounded semaphore checks to make sure its
# current value doesn't exceed its initial value.
# 5 will be the maximum value of access allowed
semaphore = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print(f"{thread_number} is trying to access!")
    # if works, acquire the semaphore decrease counter by 1
    semaphore.acquire()
    print(f"{thread_number} was granted!")
    time.sleep(10)
    print(f"{thread_number} is releasing!")
    semaphore.release()


for thread_number in range(10):
    # pass parameter to the access fn
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
    # upto 5 will be provided access and the other will
    # wait and get access only when 0 will release and so on
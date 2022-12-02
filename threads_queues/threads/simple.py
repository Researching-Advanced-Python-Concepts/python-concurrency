import threading
import time


def func(x):
    # 1. defining a task as a function
    time.sleep(1)
    print(f"Task {x} is done.")


# 2. creating threads
worker1 = threading.Thread(target=func, args=(1,))
worker2 = threading.Thread(target=func, args=(2,))

# 3. Starting the threads
# use execute them in same time use start func
worker1.start()
worker2.start()

import threading
import time

# 1. defining a task as a function
def func(x):
    time.sleep(1)
    print(f"Task {x} is done.")

# 2. creating threads
worker1 = threading.Thread(target=func, args=(1,))
worker2 = threading.Thread(target=func, args=(2,))

# 3. Starting the threads
worker1.start()
worker2.start()
import queue
import threading
import time


def func(q, thread_no):
    # 1. defining task as a func
    """
    Args:
        q (queue): queue of tasks
        thread_no (_type_): _description_
    """
    while True:
        # get an object from the queue
        task = q.get()
        time.sleep(2)
        # let the system know that this task is finished
        q.task_done()
        print(f"Thread #{thread_no} is doing task #{task} in the queue.")


# This is FIFO queue
q = queue.Queue()


for i in range(4):
    # 2. Creating a thread
    worker = threading.Thread(
        target=func,
        args=(
            q,
            i,
        ),
        daemon=True,
    )
    # if we don't specify daemon the program won't end
    worker.start()

# initially the queue is empty so our 4 threads are waiting.
# as sson as the task is inserted inside the queue, the threads start
# processing the task.
for j in range(10):
    q.put(j)

# ends the program as soon as all the jobs inside the queue are done
# and it becomes empty
# join also means don't go the next statement until it's finished
q.join()

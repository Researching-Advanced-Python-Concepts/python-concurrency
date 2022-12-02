# sometimes we may need threads to wait for some condition within
# a critical section before continuing
# done via mutual exclusion lock to protect the critical section

# if we didn't use condition, threads waiting for the condition would
# have to spin(execute in a loop) repeatedly releasing/re-acquiring the
# mutex lock until the condition was met
# ====>alternative to this is to use a condition(aka monitor) that builds
# upon a mutex and allows threads to wait and be notified
from time import sleep
from threading import Thread, Condition


# target function to prepare some work
def task(condition, work_list):
    # block for a moment
    sleep(1)
    # add data to the work list
    work_list.append(204)
    # notify a waiting thread that the work is done
    print('Thread sending notification...')
    with condition:
        condition.notify()


# create a condition
condition = Condition()
# prepare the work list
work_list = list()
# wait to be notified that the data is ready
print('Main thread waiting for data...')
# condition acquire, not doing this might cause race condition
with condition:
    # start a new thread to perform some work
    worker = Thread(target=task, args=(condition, work_list))
    worker.start()
    # wait to be notified
    condition.wait()
# we know the data is ready
print(f'Got data: {work_list}')

# the new thread is defined and started. The threads block for a moment,
# adds data to the list then notifies the waiting thread

# the main thread waits to be notified by the new threads, then once
# notified it knows the data is ready and reports the results
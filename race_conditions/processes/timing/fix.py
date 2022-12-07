# allow the notifying process to wait for the waiting process
# to be ready b4 doing its work and calling notify()

# use multiprocessing.Event which is process safe boolean flag variable
# the shared multiprocessing.Event can be passed to the task fn
# as an argument and then set by the child process while holding
# the multiprocessing.Condition, right before waiting on the condition

# event is set while the condition is held as it blocks the main
# process from acquiring the condition and calling notify until the
# child process releases the condition when calling wait()
from time import sleep
from multiprocessing import Process
from multiprocessing import Condition
from multiprocessing import Event


# process waiting to be notified
def task(condition, event):
    # insert a delay
    sleep(1)
    # wait to be notified
    print("Process: Waiting to be notified...", flush=True)
    with condition:
        # report signal that we are ready
        print("Process: Ready", flush=True)
        event.set()
        # wait to be notified
        condition.wait()
    print("Process: Notified", flush=True)


# protect the entry point
if __name__ == '__main__':
    # create the shared condition variable
    condition = Condition()
    # create the shared event
    event = Event()
    # create the new process
    process = Process(target=task, args=(condition, event))
    # start the new process
    process.start()
    # allow the new process to start up, but not start waiting
    sleep(0.5)
    # wait for the task to signal that it's ready
    event.wait()
    # notify the new process
    print('Main: Notifying the process')
    with condition:
        condition.notify()
    # wait for the task to complete
    process.join()
    print('Main: Done')

# new child process created waits for 1 sec
# the main process waits for .5 sec finishes first and then waits for event
# the child process holds the condition and then sets the event and waits
# the main process after getting the event acquires the condition
# and notifies the child process

# NO race condition 
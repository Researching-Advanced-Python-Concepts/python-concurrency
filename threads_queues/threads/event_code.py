import threading

# trigger and wait for this event
# is an element or object that has a function to be triggered.
# this triggering allows something to happen
event = threading.Event()


def func():
    print("Waiting for event to trigger...")
    # make the func wait until the event is triggered
    event.wait()
    print("Performing action for the func...")


worker1 = threading.Thread(target=func)
# we run a thread worker1 which waits for this event to trigger
worker1.start()

x = input("Do you want the event to trigger (y/n)")
if x == "y":
    # trigger the event with set()
    event.set()

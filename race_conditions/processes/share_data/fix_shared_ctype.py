# fix the race condition with shared mutex lock
# 1. we can create a mutex lock in the main process and share it
#   with each child process so they need to acquire the lock
#   before making changes
# 2. This isn't necessary as shared ctype Value and Array objects will
#   create and manage their own internal mutex lock
#   use get_lock() to retrieve the lock

from multiprocessing import Process, Value


# make addition into the shared variable
def adder(variable):
    for _ in range(1000):
        # acquire the lock on the variable
        with variable.get_lock():
            # increment the variable
            variable.value += 1


# make subtractions from the shared variable
def subtractor(variable):
    for _ in range(1000):
        with variable.get_lock():
            # decrement the variable
            variable.value -= 1


if __name__ == "__main__":
    # create a shared ctype integer
    # signed int with inital value 0
    variable = Value("i", 0)
    # start a thread making additions
    adder_thread = Process(target=adder, args=(variable,))
    adder_thread.start()

    # start a thread making subtractions
    subtractor_thread = Process(target=subtractor, args=(variable,))
    subtractor_thread.start()

    # wait for both processes to finish
    print("Waiting for processes to finish")
    adder_thread.join()
    subtractor_thread.join()

    # report the value
    print(f"Value: {variable.value}")

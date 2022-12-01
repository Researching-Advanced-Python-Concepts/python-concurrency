# 1. Read the current value of the variable
# 2. Calculate a new value for the variable
# 3. Write a new value for the variable
# context can be switched betn threads by OS in any of the steps

# can be fixed with a mutex lock
from threading import Thread


# define the global variable
value = 0


# make additon into the global variable
def adder(amount, repeats):
    global value
    for _ in range(repeats):
        value += amount


# make subtractions from the global variable
def subtractor(amount, repeats):
    global value
    for _ in range(repeats):
        value -= amount


# start a thread making addition
adder_thread = Thread(target=adder, args=(100, 1_000_000))
adder_thread.start()


# start a thread making subtractions
subtractor_thread = Thread(target=subtractor, args=(100, 1_000_000))
subtractor_thread.start()

# the main thread will wait fro both adder and subtractor threads to finish
# before reporting the final value of the shared variable
# wait for both threads to finish
print("Waiting for threads to finish")
adder_thread.join()
subtractor_thread.join()

# report the value
print(f"Value: {value}")


# Interesting thing happens:
# on running on windows the value isn't 0, the value fluctuates
# but running on ubuntu machine the value is always 0

# found it: race condition is caused in Python 3.9 and below but
# not in Python 3.10 and above

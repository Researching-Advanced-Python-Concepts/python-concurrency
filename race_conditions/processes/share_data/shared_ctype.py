# Another processes is by using shared ctypes

# python provides the capabiility yo share ctypes betn processes
# on one system

# multiprocessing.Value: manage a shared value
# multiprocessing.Array: manage an array of shared values
from multiprocessing import Process, Value


# make addition into the shared variable
def adder(variable):
    for _ in range(1000):
        # increment the variable
        variable.value += 1


# make subtractions from the shared variable
def subtractor(variable):
    for _ in range(1000):
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

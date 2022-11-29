import queue

example_FIFO = queue.Queue()
example_LIFO = queue.LifoQueue()
# we can also set the size for the queue
example_Prio = queue.PriorityQueue(10)


# insert into queue use put()
# call an obj. from the queue using get()

print("********** FIFO **********")
for i in range(5):
    example_FIFO.put(i)

# for i in range(5):
#     print(example_FIFO.get())

# in real world we don't know the no. of items in the queue
# so we must loop through all items inside a queue until the queue
# becomes empty
# use empty() to check if the queue is empty or not (boolean result)

# Making upper code better
while not example_FIFO.empty():
    print(example_FIFO.get())



print("********** LIFO **********")
for i in range(5):
    example_LIFO.put(i)

while not example_LIFO.empty():
    print(example_LIFO.get())


print("********** Priority queue **********")
for i in range(5):
    names = ["mikeyy", "mickey", "maus", "mouse", "musha"]
    example_LIFO.put((4 - i, names[i]))

while not example_LIFO.empty():
    print(example_LIFO.get())



# daemon threads are running in the background and the script terminates
# even though they're still running because they're not vital to the
# program

# if we have a couple of threads running program usually waits for all
# these threads to finish to be stopped but nobody waits for dameon threads
# daemon threads will close after the program terminates

import threading
import time


path = "text.txt"
text = ""


def readFile():
    # readFile in the daemon thread so its not important
    # we can just termindate the loop without terminating it
    # manually
    global path, text
    while True:
        with open(path) as f:
            text = f.read()
        time.sleep(3)


def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()

# we can just change the text and the daemon thread will read that also

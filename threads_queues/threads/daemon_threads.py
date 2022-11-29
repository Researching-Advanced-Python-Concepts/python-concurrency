# daemon threads are running in the background and the script terminates
# even though they're still running because they're not vital to the
# program

# if we have a couple of threads running program usually waits for all
# these threads to finish to be stopped but nobody waits for dameon threads
# daemon threads will close after the program terminates

import threading
import time


# python-concurrency

Learn how python concurrency works via codes

- [for more information](https://realpython.com/python-concurrency/)

## I/O Bound Process

- Here our program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
- We can speed it up by overlapping the times spent waiting for these devices.
  - While a web connection is being made we can do some other tasks in the mean time
  - While downloading webpages from a few sites other tasks can be run
  - When a file is being read
  - These tasks take relatively more time so some other tasks can be incorporated in that time frame.


# python-concurrency

Learn how python concurrency works via codes

- [for more information](https://realpython.com/python-concurrency/)

## I/O Bound Process

- Here our program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
- We can speed it up by overlapping the times spent waiting for these devices.
  - While a web connection is being made we can do some other task in the mean time

# python-concurrency

Learn how python concurrency works via codes

- [for more information](https://realpython.com/python-concurrency/)

## Asyncio Semaphore

- [reasoning-about-asynciosemaphore](https://neopythonic.blogspot.com/2022/10/reasoning-about-asynciosemaphore.html)
- if u see a seat that's not in use it's already reserved for someone who got in line first

## I/O Bound Process

- Here our program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
- We can speed it up by overlapping the times spent waiting for these devices.
  - While a web connection is being made we can do some other tasks in the mean time
  - While downloading webpages from a few sites other tasks can be run
  - When a file is being read
  - These tasks take relatively more time so some other tasks can be incorporated in that time frame.

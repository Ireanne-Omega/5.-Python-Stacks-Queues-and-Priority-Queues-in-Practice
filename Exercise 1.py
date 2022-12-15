# queues.py

from collections import deque

# Exercise 1
class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# Exercise 2

from queue import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

fifo.dequeue()
'1st'
fifo.dequeue()
'2nd'
fifo.dequeue()
'3rd'











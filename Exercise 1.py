# queues.py


# Exercise 1

class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


# Exercise 2

from queues import Queue

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

# Exercise 3

from collections import deque


class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


# Exercise 4

fifo: Queue
from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

len(fifo)

for element in fifo:
    print(element)

len(fifo)


# Exercise 5

class Stack(Queue):
    def __init__(self, *elements):
        super().__init__(elements)
        self._elements = None

    def dequeue(self):
        return self._elements.pop()


# Exercise 6

from queues import Stack

lifo = Stack("1st", "2nd", "3rd")

for element in lifo:
    print(element)

# Exercise 7

lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

lifo.pop()
lifo.pop()
lifo.pop()

# Exercise 8

from heapq import heappush

fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

fruits


# Exercise 9

from heapq import heappop

heappop(fruits)

fruits


# Exercise 10

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

person1 < person2
#True

person2 < person3
#False








# Programmed by: Ireanne N. Omega BSCOE 2-2
# Reference: https://realpython.com/queue-in-python/#learning-about-the-types-of-queues

# Exercise 1
# QUEUES

# this is for importing and refactoring
from collections import deque

class IterableMixin:
    class IterableMixin:
        def __len__(self):
            return len(self._elements)

        def __iter__(self):
            while len(self) > 0:
                yield self.dequeue()

    class Queue(IterableMixin):
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


# Exercise 2
# FIFO QUEUES FIRST EXAMPLE

# enqueue statement
class Queue:
    pass

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# dequeue statement
fifo.dequeue()
fifo.dequeue()
fifo.dequeue()


# Exercise 3
# FIFO QUEUE SECOND EXAMPLE

fifo: Queue
from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

len(fifo)

for element in fifo:
    print(element)

len(fifo)

# Exercise 4
# Class Queue and Input Statement

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


# Exercise 5
# Stack Data Type Queues

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


# Exercise 6
# Lifo Queue First Example

lifo = Stack("1st", "2nd", "3rd")

for element in lifo:
    print(element)


# Exercise 7
# Lifo Queue Second Example

lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

lifo.pop()
lifo.pop()
lifo.pop()


# Exercise 8
# Priority Queue & Heap & Heappush

# this is for importing and refactoring
from heapq import heappush


#Heappush
fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

fruits


# this is for importing and refactoring
from heapq import heappop


# Heappop
heappop(fruits)

fruits


# Exercise 10
# Tuple Comparison

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

person1 < person2

person2 < person3


# Exercise 11
# Priority Queue Data Type

# this is for importing and refactoring
from collections import deque
from heapq import heappop, heappush


class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)[1]
    

# Exercise 12
# Priority Queue Data Type First Example

from queues import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()

messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

messages.dequeue()

messages.dequeue()

messages.dequeue()

messages.dequeue()


# Exercise 13
# Corner Cases in the Priority Queue

# this is for importing and refactoring
from collections import deque
from heapq import heappop, heappush
from itertools import count

class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]


# Exercise 14
# Data Classes

# this is for importing and refactoring
from dataclasses import dataclass

@dataclass
class Message:
    event: str


# Exercise 15

# this is for importing and refactoring
from dataclasses import dataclass

@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")


# Exercise 16
# Messages

messages = PriorityQueue()

messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))



















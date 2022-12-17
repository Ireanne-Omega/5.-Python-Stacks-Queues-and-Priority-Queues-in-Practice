# Exercise 2
# FIFO QUEUES FIRST EXAMPLE

# enqueue statement
from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# dequeue statement
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())

# Exercise 3
# FIFO QUEUE SECOND EXAMPLE

from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

print(len(fifo))

for element in fifo:
    print(element)

print(len(fifo))


# Exercise 6
# Lifo Queue First Example
from queues import Stack

lifo = Stack("1st", "2nd", "3rd")

for element in lifo:
    print(element)

# Exercise 7
# Lifo Queue Second Example

lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo.pop())
print(lifo.pop())
print(lifo.pop())

# Exercise 8
# Priority Queue & Heap & Heappush

# this is for importing and refactoring
from heapq import heappush

# Heappush
fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

# this is for importing and refactoring
from heapq import heappop

# Heappop
print(heappop(fruits))

print(fruits)

# Exercise 10
# Tuple Comparison

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1 < person2)

print(person2 < person3)


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

print(messages.dequeue())

print(messages.dequeue())

print(messages.dequeue())

print(messages.dequeue())


# Exercise 16
# Messages

from dataclasses import dataclass


@dataclass
class Message:
    event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")


messages = PriorityQueue()

messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())


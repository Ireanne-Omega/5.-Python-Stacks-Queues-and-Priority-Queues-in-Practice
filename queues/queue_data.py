from queues import Queue

fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

fifo.dequeue()

fifo.dequeue()

fifo.dequeue()


from queues import Queue

fifo = Queue()
fifo.enqueue("red")
fifo.enqueue("yellow")
fifo.enqueue("blue")

fifo.dequeue()
fifo.dequeue()
fifo.dequeue()

fifo = Queue("red", "yellow", "blue")
len(fifo)

for element in fifo:
     print(element)
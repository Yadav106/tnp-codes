class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.size

    def peek(self):
        if self.is_empty():
            print("Can't peek, queue is empty")
            return
        print("peek : ", self.queue[0])
        return self.queue[0]

    def enqueue(self, val):
        if self.is_full():
            print("Can't enqueue data, queue is full")
            return
        print("enqueueing", val)
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            print("Can't pop, queue is empty")
            return
        print("dequeuing")
        self.queue.pop(0)

my_queue = Queue(3)
my_queue.peek()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.peek()
my_queue.dequeue()
my_queue.peek()

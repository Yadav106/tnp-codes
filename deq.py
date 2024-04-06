class DoubleEndedQueue:
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

    def append_left(self, val):
        if self.is_full():
            print("Can't append left data, queue is full")
            return
        print("appending to left", val)
        self.queue = [val] + self.queue
        self.print_deq()

    def remove_left(self):
        if self.is_empty():
            print("Can't remove left, queue is empty")
            return
        print("removing from left")
        self.queue.pop(0)
        self.print_deq()

    def append_right(self, val):
        if self.is_full():
            print("Can't append left data, queue is full")
            return
        print("appending to right", val)
        self.queue.append(val)
        self.print_deq()

    def remove_right(self):
        if self.is_empty():
            print("Can't remove left, queue is empty")
            return
        print("removing from left")
        self.queue.pop(len(self.queue)-1)
        self.print_deq()

    def print_deq(self):
        for i in self.queue:
            print(f"| {i} |", end="")
        print("")

my_queue = DoubleEndedQueue(3)
my_queue.peek()
my_queue.append_left(1)
my_queue.append_left(2)
my_queue.append_right(3)
my_queue.append_left(4)
my_queue.peek()
my_queue.remove_left()
my_queue.peek()

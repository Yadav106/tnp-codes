class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def push(self, x):
        if self.isFull():
            print("Can't push on stack, max size reached")
            return
        print(f"Pushing {x}")
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            print("Can't pop from stack. Stack is empty")
            return 
        print(f"Popping {self.stack[-1]}")
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) == self.size

my_stack = Stack(5)
print("Top of the stack : ", my_stack.peek())
my_stack.push(1)
my_stack.push(2)
print("Top of the stack : ", my_stack.peek())
my_stack.pop()
print("Top of the stack : ", my_stack.peek())
my_stack.pop()
my_stack.pop()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)


class MultiStack:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.ds = [None] * (size*quantity)
        print(f"Made {quantity} stacks")

    def find_limits(self, stack):
        low = ((stack-1) * self.size)
        high = (stack * self.size) - 1
        return (low, high)

    def find_topmost_value(self, stack):
        low, high = self.find_limits(stack)
        for i in range(low, high+1):
            if self.ds[i] == None:
                return i, high, low
        return high+1, high, low

    def is_full(self, stack):
        ind, high, _ = self.find_topmost_value(stack)
        return ind > high

    def is_empty(self, stack):
        ind, _, low = self.find_topmost_value(stack)
        return ind == low

    def push(self, stack, value):
        if self.is_full(stack):
            print(f"Can't push on stack, stack {stack} full")
            return
        pos, _, _ = self.find_topmost_value(stack)
        print(f"Pushing {value} on stack {stack}")
        self.ds[pos] = value

    def pop(self, stack):
        if self.is_empty(stack):
            print(f"Can't pop from stack {stack}")
        ind, _, _ = self.find_topmost_value(stack)
        ind -= 1
        print(f"Popping from stack {stack}")
        self.ds[ind] = None

    def peek(self, stack):
        ind, _, _ = self.find_topmost_value(stack)
        if self.is_full(stack):
            ind -= 1
        return self.ds[ind]



stacks = MultiStack(3, 3)
stacks.push(1, 1)
stacks.push(1, 2)
stacks.push(1, 3)
stacks.push(1, 4)
stacks.push(2, 4)
stacks.push(2, 5)
stacks.push(2, 6)
stacks.push(2, 7)
stacks.push(3, 7)
stacks.push(3, 8)
stacks.push(3, 9)
stacks.push(3, 10)

print(f"peeking stack 3 : {stacks.peek(3)}")

stacks.pop(3)
stacks.push(3, 10)
stacks.push(3, 11)
print(stacks.peek(3))

print(f"peeking stack 2 : {stacks.peek(2)}")
stacks.pop(2)
stacks.push(2, 11)
print(f"peeking stack 2 : {stacks.peek(2)}")


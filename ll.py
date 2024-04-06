class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node = Node(value)
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def __str__(self):
        if self.head == None:
            return "Linked List is empty" 
        trav = self.head
        res = ""
        while(trav is not None):
            temp_str = f"{trav.value} -> "
            trav = trav.next
            res = res + temp_str
        res = res + "None"
        return res

ll = LinkedList()
print(ll)
ll.append(10)
print(ll)
ll.append(20)
print(ll)
ll.prepend(0)
print(ll)
ll.prepend(-10)
print(ll)
ll.insert(1, -5)
print(ll)

# Implement a stack using a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def peek(self):
        return self.head.data

    def __len__(self):
        return self.size


my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(len(my_stack))  
print(my_stack.peek())

item = my_stack.pop()
print(item)

print(len(my_stack))
from homework25 import *
# task_2


class Stack:

    def __init__(self):  # initialize the empty list UnorderedList
        self.items = UnorderedList()

    def is_empty(self):  # check if the stack is empty
        return self.items.is_empty()

    def push(self, item):  # add an element to the beginning of the list
        return self.items.add(item)

    def pop(self):
        if self.is_empty():  # if stack is empty, raise IndexError
            raise IndexError('Stack is empty.')
        return self.items.pop(0)  # remove and return the element from the beginning of the list

    def peek(self):
        if self.is_empty():  # if stack is empty, raise IndexError
            raise IndexError('Stack is empty.')
        return self.items.head.data  # return the element from the beginning of the list

    def size(self):
        return self.items.size()  # return the number of elements in the stack


stack = Stack()
print(stack.is_empty())  # True
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())  # 30
print(stack.size())  # 3
print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.is_empty())  # False



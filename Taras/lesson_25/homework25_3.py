from homework25 import *


class Queue:

    def __init__(self):
        self.items = UnorderedList()  # initialize the empty list UnorderedList

    def is_empty(self):
        return self.items.is_empty()  # check if the queue is empty

    def enqueue(self, item):
        return self.items.append(item)  # add an element to the end of the queue

    def dequeue(self):
        if self.is_empty():  # if the queue is empty, raise IndexError
            raise IndexError('Queue is empty.')
        return self.items.pop(0)  # remove and return the first element of the queue

    def size(self):
        return self.items.size()  # return the number of elements in the queue


queue = Queue()
print(queue.is_empty())  # True
queue.enqueue('Garrosh')
queue.enqueue('Thrall')
queue.enqueue("Vol'jin")
print(queue.size())  # 3
print(queue.dequeue())  # Garrosh
print(queue.size())  # 2
print(queue.is_empty())  # False






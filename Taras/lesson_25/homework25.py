# task_1
class UnorderedList:

    def __init__(self):
        self.head = None  #  initialize the head of the list as None

    def is_empty(self):  # check whether the list is empty by checking if the head is None
        return self.head is None  # return True if the list is empty, and False otherwise.

    def add(self, item):  # add a new item to the beginning of the list
        temp = Node(item)  # create a new Node object with the given item
        temp.next = self.head  # set Node object next reference to the current head
        self.head = temp  # update the head to point to the new node

    def size(self):  # return the number of items in the list
        current = self.head
        count = 0
        while current is not None:  # traverse the list starting from the head and increments a counter for each node
            # until the end of the list is reached.
            count += 1
            current = current.next
        return count

    def append(self, item):  # add a new item to the end of the list
        temp = Node(item)  # create a new Node object with the given item
        if self.is_empty():  # if the list is empty, it sets the head to the new node
            self.head = temp
        else:  # otherwise, traverse the list until the last node is reached and append the new node as the next
            # reference of the last node
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    def index(self, item):  # return the index of the first occurrence of the given item in the list
        current = self.head  # start from the head and iterates through the list
        index = self.size() - 1
        while current is not None:
            if current.data == item:  # if the item is found, it returns the index
                return index
            current = current.next
            index -= 1
        raise ValueError(f"Item '{item}' not found in the list.")  # if the item is not found, raise a ValueError
    # def index(self, item):
    #       test
    #     current = self.head
    #     index = 0
    #     while current is not None:
    #         if current.data == item:
    #             return index
    #         current = current.next
    #         index += 1
    #     raise ValueError(f"Item '{item}' not found in the list.")

    def pop(self, pos = None):  # remove and return the item at the specified position in the list
        if self.is_empty():   # if the list is empty, it raise an IndexError
            raise IndexError("Can't pop from an empty list.")
        if pos is None:  # if the pos parameter is not provided, it defaults to the last position in the list
            pos = self.size() - 1
        if pos < 0 or pos >= self.size():  # if the pos parameter is less than 0 or greater than or equal to the size
            # of the list, it raise an IndexError
            raise IndexError('Index out of range.')
        if pos == 0:  # if pos is 0, it mean the item to be popped is the first item in the list
            item = self.head.data  # assign the current head's data to item
            self.head = self.head.next  # update the head to the next node
            return item  # return item
        current = self.head
        previous = None
        index = 0
        while current is not None and index < pos:  # set up a loop to traverse the list until the desired position is
            # reached
            previous = current  # keep track of the previous node, the current node, and the index of the current node
            current = current.next
            index += 1
        item = current.data  # assigns the current node's data to item
        previous.next = current.next  # update the next reference of the previous node to skip the current node,
        # effectively removing it from the list
        return item  # return item, which is the item that was popped from the list

    def insert(self, pos, item):  # insert the item at the specified position in the list
        if pos < 0 or pos > self.size():  # if the pos parameter is less than 0 or greater than the size of the list,
            # raise an IndexError
            raise IndexError('Index out of range.')
        if pos == 0:  # if pos is 0, it means the item is to be inserted at the beginning of the list
            self.add(item)
        else:
            temp = Node(item)  # if pos is not 0, the method create a new Node object temp with the given item
            current = self.head
            previous = None
            index = 0
            while current is not None and index < pos:  # set up a loop to traverse the list until the desired position
                # is reached
                previous = current  # keep track of the previous node, the current node, and the index of the current
                # node
                current = current.next
                index += 1
            previous.next = temp  # update the next reference of the previous node to point to temp, effectively
            # inserting temp between previous and current
            temp.next = current

    def slice(self, start, stop):  # return a new UnorderedList object that contains a slice of the original list
        if start < 0 or stop > self.size() or start >= stop:  # if the start or stop values are invalid, raise ValueErro
            raise ValueError('Invalid slice range.')
        result = UnorderedList()  # create a new UnorderedList object result to store the sliced elements
        current = self.head  # initialize current as the head of the original list and index as 0
        index = 0
        while current is not None and index < stop:  # iterate over the elements of the original list
            if index >= start:  # if the current index is within the desired slice range
                result.append(current.data)  # append the current element's data to the result list
            current = current.next  # update current to the next node and increments index
            index += 1
        return result


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    my_list = UnorderedList()
    my_list.add(10)
    my_list.add(20)
    my_list.add(30)
    print(f'Size: {my_list.size()}')  # Size 3
    print(f'Index of 30: {my_list.index(30)}')  # Index of 30: 2
    my_list.append(40)
    item = my_list.pop(1)
    print(f'Popped item: {item}')  # 20
    my_list.insert(1, 50)
    new_list = my_list.slice(0, 3)
    print('New list:', end=' ')
    current = new_list.head
    while current is not None:
        print(current.data, end=' ')
        current = current.next  # New list: 30 50 10

# тема пішла доволі важко. Потрібно буде ще читати/дивитися щось, мабуть. Довелося просити допомоги з вирішенням цієї
# задачі :/

# task_2
# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#
#     def __init__(self):  # initialize the top of the stack as None. This indicates an empty stack
#         self.top = None
#
#     def is_empty(self):  # return True if the top of the stack is None, indicating an empty stack, and False otherwise
#         return self.top is None
#
#     def push(self, item):
#         new_node = Node(item)  # create a new node with the given item
#         if self.is_empty():  # if the stack is empty, the new node becomes the top of the stack
#             self.top = new_node
#         else:  # otherwise, the new node's next reference is set to the current top
#             new_node.next = self.top
#             self.top = new_node  # the new node becomes the new top of the stack
#
#     def pop(self):
#         if self.is_empty():  # if the stack is empty, raise an IndexError
#             raise IndexError('Stask is empty.')
#         item = self.top.data  # data value of the top node is assigned to the variable item
#         self.top = self.top.next  # the top is updated to the next node in the stack, effectively removing the current
#         # top node
#         return item  # return the item that was removed
#
#     def peek(self):  # return the item at the top of the stack without removing it
#         if self.is_empty():  # if the stack is empty, raise an IndexError
#             raise IndexError('Stack is empty.')
#         return self.top.data  # return the data value of the top node
#
#     def size(self):
#         count = 0  # initialize a counter variable count to 0
#         current = self.top  # set current to the top node
#         while current is not None:  # iterate through the stack by moving current to the next node until it reaches
#             # the end
#             count += 1  # for each iteration, it increments count by 1
#             current = current.next
#         return count  # return the total count
#
#
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.peek())  # 30
# print(stack.size())  # 3
# print(stack.pop())  # 30
# print(stack.pop())  # 20
# print(stack.is_empty())  # False

# task_3
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Queue:
#     def __init__(self):  # initialize front and rear of the queue
#         self.front = None
#         self.rear = None
#
#     def is_empty(self):  # check if the queue is empty by verifying if the front is None
#         return self.front is None
#
#     def enqueue(self, item):  # add an item to the rear of the queue
#         new_node = Node(item)  # create a new node with the given item
#         if self.is_empty():  # if the queue is empty, both front and rear are set to the new node since it will be the
#             # only item in the queue
#             self.front = new_node
#             self.rear = new_node
#         else:  # otherwise, the new node is linked to the current rear node, and rear is updated to the new node
#             self.rear.next = new_node
#             self.rear = new_node
#
#     def dequeue(self):
#         if self.is_empty():  # check if the queue is empty. If it is empty, raise an IndexError
#             raise IndexError('Queue is empty.')
#         item = self.front.data  # retrieve the data from the front node
#         self.front = self.front.next  # update the front to the next node
#         if self.front is None:  # check if the queue became empty after the removal
#             self.rear = None  # If the queue is empty, both front and rear are set to None
#         return item  # return the removed item
#
#     def peek(self):
#         if self.is_empty():  # check if the queue is empty. If it is empty, raise an IndexError
#             raise IndexError('Queue is empty.')
#         return self.front.data  # otherwise, return the data of the front node
#
#     def size(self):
#         count = 0  # initialize a count variable to 0
#         current = self.front  # set current to the front node
#         while current is not None:  # iterate through the linked list
#             count += 1  # incrementing count by 1 for each node until current becomes None
#             current = current.next
#         return count
#
#
# queue = Queue()
# queue.enqueue('A')
# queue.enqueue('B')
# queue.enqueue('C')
# queue.enqueue('D')
# print(f'Size of the queue: {queue.size()}')  # 4
# print(f'Front item: {queue.peek()}')  # A
# print(f'Dequeued item: {queue.dequeue()}')  # A
# print(f'Dequeued item: {queue.dequeue()}')  # B
# queue.enqueue('E')
# print(f'Dequeued item: {queue.dequeue()}')  # C
# print(f'Dequeued item: {queue.dequeue()}')  # D
# print(f'Dequeued item: {queue.dequeue()}')  # E
# print(f'Empty? {queue.is_empty()}')  # True

# from node import Node
#
#
# class UnorderedList:
#
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         return self._head is None
#
#     def add(self, item):
#         temp = Node(item)
#         temp.set_next(self._head)
#         self._head = temp
#
#     def size(self):
#         current = self._head
#         count = 0
#         while current is not None:
#             count += 1
#             current = current.get_next()
#
#         return count
#
#     def search(self, item):
#         current = self._head
#         found = False
#         while current is not None and not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 current = current.get_next()
#
#         return found
#
#     def remove(self, item):
#         current = self._head
#         previous = None
#         found = False
#         while not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.get_next()
#
#         if previous is None:
#             self._head = current.get_next()
#         else:
#             previous.set_next(current.get_next())
#
#     def append(self, item):
#         temp = Node(item)
#         if self.is_empty():
#             self._head = temp
#         else:
#             current = self._head
#             while current.get_next() is not None:
#                 current = current.get_next()
#             current.set_next(temp)
#
#     def index(self, item):
#         current = self._head
#         index = 0
#         while current is not None:
#             if current.get_data() == item:
#                 return index
#             current = current.get_next()
#             index += 1
#
#     def pop(self, index=None):
#         if index == None:
#             index = self.size() - 1
#         if index < 0 or index >= self.size():
#             raise IndexError('Index out of range')
#
#         current = self._head
#         previous = None
#         current_index = 0
#         while current_index < index:
#             previous = current
#             current = current.get_next()
#             current_index += 1
#
#         if previous is None:
#             self._head = current.get_next()
#         else:
#             previous.set_next(current.get_next())
#
#         return current.get_data()
#
#     def insert(self, index, item):
#         if index < 0 or index > self.size():
#             raise IndexError("insert index out of range.")
#
#         if index == 0:
#             self.add(item)
#         else:
#             temp = Node(item)
#             current = self._head
#             previous = None
#             current_index = 0
#             while current_index < index:
#                 previous = current
#                 current = current.get_next()
#                 current_index += 1
#             previous.set_next(temp)
#             temp.set_next(current)
#
#     def slice(self, start, stop):
#         temp_list = UnorderedList()
#         current = self._head
#         index = 0
#         while index < start:
#             current = current.get_next()
#             index += 1
#         while index < stop and current is not None:
#             temp_list.append(current.get_data())
#             current = current.get_next()
#         return temp_list
#
#     def __repr__(self):
#         representation = "<UnorderedList: "
#         current = self._head
#         while current is not None:
#             representation += f"{current.get_data()} "
#             current = current.get_next()
#         return representation + ">"
#
#     def __str__(self):
#         return self.__repr__()
#
# class Stack:
#     def __init__(self):
#         self._items = UnorderedList()
#
#     def is_empty(self):
#         return self._items.is_empty()
#
#     def push(self, item):
#         self._items.add(item)
#
#     def pop(self):
#         return self._items.pop(0)
#
#     def peek(self):
#         return self._items.index(0)
#
#     def size(self):
#         return self._items.size()
#
#
#     def __repr__(self):
#         return self._items.__repr__()
#
#     def __str__(self):
#         return self.__repr__()
#
# class Queue:
#     def __init__(self):
#         self._items = UnorderedList()
#
#     def is_empty(self):
#         return self._items.is_empty()
#
#     def enqueue(self, item):
#         self._items.append(item)
#
#     def dequeue(self):
#         return self._items.pop(0)
#
#     def size(self):
#         return self._items.size()
#
#     def __repr__(self):
#         return self._items.__repr__()
#
#     def __str__(self):
#         return self.__repr__()
#
#
# if __name__ == "__main__":
#     # Task 1
#     my_list = UnorderedList()
#     my_list.add(1)
#     my_list.add(2)
#     my_list.add(3)
#     my_list.append(7)
#     print(my_list)
#     print(my_list.index(1))
#
#     print(my_list.pop(1))
#     print(my_list)
#     my_list.insert(1, 10)
#     print(my_list)
#     print()
#     print(my_list.slice(1, 2))
#     print(my_list.index(10))
#     # Task 2
#     s = Stack()
#     some = 'qwerty'
#     for _ in some:
#         s.push(_)
#     print(s)
#     print(s.pop())
#     print(s.peek())
#     s.push('la-la')
#     print(s)
#     # Task 3
#     q = Queue()
#     q.enqueue(4)
#     q.enqueue('dog')
#     q.enqueue(True)
#     print(q)
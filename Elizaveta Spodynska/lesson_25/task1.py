# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position and going up to but not including the stop position.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def pop(self, pos=None):
        if pos is None:
            if self.head.next is None:
                item = self.head.data
                self.head = None
                return item
            else:
                current = self.head
                while current.next.next is not None:
                    current = current.next
                item = current.next.data
                current.next = None
                return item
        else:
            if pos < 0:
                raise IndexError("Negative index is not valid.")
            if pos == 0:
                item = self.head.data
                self.head = self.head.next
                return item

            current = self.head
            prev = None
            index = 0
            while current is not None and index < pos:
                prev = current
                current = current.next
                index += 1

            if current is None:
                raise IndexError("Index is not valid")

            item = current.data
            prev.next = current.next
            return item

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError('item is not in the list')

    def slice(self, start, stop):
        if start < 0 or stop < 0:
            raise IndexError("Negative index is not allowed.")
        if start >= stop:
            return UnorderedList()

        current = self.head
        index = 0
        while current is not None and index < start:
            current = current.next
            index += 1

        if current is None and index != start:
            raise IndexError("Start index is not valid")

        new_list = UnorderedList()
        while current is not None and index < stop:
            new_list.append(current.data)
            current = current.next
            index += 1

        return new_list

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, pos, item ):
        new_node = Node(item)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(pos - 1):
                if current.next:
                    current = current.next
                else:
                    raise IndexError('Position not valid')
            new_node.next = current.next
            current.next = new_node


my_list = UnorderedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)

print(my_list.index(30))

print(my_list.pop())
print(my_list.pop(1))

my_list.insert(1, 25)



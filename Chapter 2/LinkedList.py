from random import randint

class Node:
    def __init__(self, value, nextNode = None, prevNode= None):
        self.value = value
        self.prev = prevNode
        self.next = nextNode

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def __str__(self):
        values = [str(x) for x in self]
        return '->'.join(values)

    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(values)

    def generate(self, length, min_val, max_val):
        self.head = self.tail = None
        for i in range(length):
            self.add(randint(min_val, max_val))
        return self

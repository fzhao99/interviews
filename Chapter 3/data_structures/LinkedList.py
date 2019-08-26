from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values:
            self.add_multiple(i)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter +=1
            current = current.next
        return counter

    def __str__(self):
        values = [str(x) for i in self]
        return '-->'.join(values)

    def add(self, value):
        item = Node(value)
        if self.tail:
            self.tail.next = item
            self.tail = item
        else:
            self.head = self.tail = item

    def add_to_beginning(self, value):
        item = Node(value)
        self.head.prev = item
        item.next = self.head
        self.head = item

    def add_multiple(self, values):
        for i in values:
            add(i)

    def generate(self, length, min_val, max_val):
        self.head = self.tail= None
        for _ in range(length):
            node = Node(randint(min_val,max_val))
            self.add(node)
        return self

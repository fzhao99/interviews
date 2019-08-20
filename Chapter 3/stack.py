import unittest

class Stack:
    class StackNode:
        def __init__(self,value):
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if self.top:
            item = self.top.value
            self.top = self.top.prev
            self.size -=1
            return self.top
        else:
            raise IndexError("Popping from empty stack")

    def push(self, value):
        item = self.StackNode(value)
        if self.top:
            item.prev = self.top
            self.top.next = item
            self.top = item
        else:
            self.top = item

        self.size +=1

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.size == 0

class Tests(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        for i in range(35):
            stack.push(i)

        for i in range(35, -1):
            self.assertEqual(stack.peek(),i)
            stack.pop()
    def test_is_empty(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)

        stack.push(5)
        self.assertEqual(stack.is_empty(), False)
if __name__=="__main__":
    unittest.main()

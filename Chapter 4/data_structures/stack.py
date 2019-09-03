import unittest

class Stack:
    class StackNode:
        def __init__(self,value):
            self.value = value
            self.above= None
            self.below = None

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def pop(self):
        if self.top:
            item = self.top
            self.top = self.top.below
            self.size -=1
            return item.value
        else:
            raise IndexError("Popping from empty stack")

    def join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def push(self, value):
        item = self.StackNode(value)
        self.size += 1

        if self.size == 1:
            self.bottom = item
        self.join(item, self.top)
        self.top = item

    def remove_bottom(self):
        bottom = self.bottom
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return bottom.value

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def is_not_empty(self):
        return self.size != 0

    def to_list(self):
        run = self.top
        lst = []
        while run:
            lst.append(run.value)
            run = run.below
        return lst

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

    def test_to_list(self):
        stack = Stack()

        for i in range(35):
            stack.push(i)

        lst = stack.to_list()
        self.assertEqual(lst, list(reversed(range(35))))

if __name__=="__main__":
    unittest.main()

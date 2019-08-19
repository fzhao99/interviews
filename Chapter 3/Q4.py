import unittest

class MyQueue:
    def __init__(self):
        self.threshold = 5
        self.stacks =[[],[]]

    def enqueue(self, item):
        self.stacks[0].append(item)

    def dequeue(self):
        self.reorder()
        if self.stacks[1]:
            return self.stacks[1].pop()
        else:
            raise IndexError("dequeing from empty list")

    def reorder(self):
        if not self.stacks[1]:
            while self.stacks[0]:
                item = self.stacks[0].pop()
                self.stacks[1].append(item)

class Tests(unittest.TestCase):
    def test_enqueue(self):
        q = MyQueue()
        for i in range(35):
            q.enqueue(i)

        lst = q.stacks[1] + q.stacks[0]
        self.assertEqual(lst, list(range(35)))

    def test_dequeue(self):
        q = MyQueue()
        for i in range(35):
            q.enqueue(i)

        lst = []
        for _ in range(35):
            item = q.dequeue()
            lst.append(item)

        self.assertEqual(lst, list(range(35)))

    def test_error_raise(self):
        q = MyQueue()
        with self.assertRaises(IndexError): q.dequeue()
if __name__ == "__main__":
    unittest.main()

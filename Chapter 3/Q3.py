import unittest

class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stack_set = []
        self.cur_stack = []

    def push(self, item):
        if len(self.cur_stack) > self.threshold:
            self.stack_set.append(self.cur_stack)
            self.cur_stack = []
        self.cur_stack.append(item)

    def pop(self):
        if len(self.cur_stack)==0 and len(self.stack_set) >0:
            self.cur_stack = self.stack_set.pop()

        return self.cur_stack.pop()

    def pop_at(self, index):
        if 0 < index < len(self.stack_set):
            return self.stack_set[index].pop()
        elif index == len(self.stack_set):
            return self.cur_stack.pop()
        else:
            raise IndexError("popping from outside stack index")


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)

        lst = []

        for _ in range(35):
            lst.append(stacks.pop())

        self.assertEqual(lst, list(reversed(range(35))))
    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        print(stacks.stack_set)
        lst = []

        for _ in range(31):
            lst.append(stacks.pop_at(0))
        self.assertEqual(lst, list(range(4,35)))

    def test_empty(self):
        stacks = SetOfStacks(1)
        with self.assertRaises(IndexError): stacks.pop()

if __name__=='__main__':
    unittest.main()

import unittest
from data_structures.stack import Stack

class SetOfStacks:
    def __init__(self, threshold):
        self.threshold = threshold
        self.stack_set = []

    def get_last_stack(self):
        try:
            return self.stack_set[-1]
        except IndexError:
            return None

    def push(self, item):
        cur_stack = self.get_last_stack()
        if cur_stack and cur_stack.size < self.threshold:
            cur_stack.push(item)

        else:
            cur_stack = Stack()
            cur_stack.push(item)
            self.stack_set.append(cur_stack)

    def pop(self):
        cur_stack = self.get_last_stack()
        if not cur_stack:
            raise IndexError
        item = cur_stack.pop()
        if cur_stack.size == 0:
            del self.stack_set[-1]
        return item

    def left_shift(self, index, remove_top):
        stack = self.stack_set[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if stack.is_empty():
            del self.stack_set[index]
        elif len(self.stack_set) > index + 1:
            v = self.left_shift(index +1, False)
            stack.push(v)
        return removed_item

    def pop_at(self, index):
        return self.left_shift(index, True)

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
        lst = []

        for _ in range(31):
            lst.append(stacks.pop_at(0))
        self.assertEqual(lst, list(range(4,35)))

    def test_empty(self):
        stacks = SetOfStacks(1)
        with self.assertRaises(IndexError): stacks.pop()

if __name__=='__main__':
    unittest.main()

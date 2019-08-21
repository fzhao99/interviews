from random import randint
import unittest

def sort_stack(stack):

class Test(unittest.TestCase):
    def test_sort(self):
        stack = []
        stack_copy = []

        for _ in range(10):
            item = randint(0,100)
            stack.append(item)
            stack_copy.append(item)

        sorted = sort_stack(stack)
        stack_copy.sort(reverse=True)
        self.assertEqual(sorted, stack_copy)


if __name__=="__main__":
    unittest.main()

from random import randint
import unittest

from stack import Stack

def sort_stack(stack):
    temp_stack = Stack()
    temp_stack.push(stack.pop())

    while not stack.is_empty():
        cur = stack.pop()
        if temp_stack.is_empty():
            temp_stack.push(cur)
        else:

            while cur < temp_stack.peek():
                stack.push(temp_stack.pop())

                if temp_stack.is_empty():
                    break

            temp_stack.push(cur)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack

class Test(unittest.TestCase):
    def test_sort(self):
        stack = Stack()
        stack_copy = Stack()

        for _ in range(10):
            item = randint(0,100)
            stack.push(item)
            stack_copy.push(item)

        sorted = sort_stack(stack).to_list()
        lst = stack_copy.to_list()
        lst.sort()
        self.assertEqual(sorted, lst)


if __name__=="__main__":
    unittest.main()

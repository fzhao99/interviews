class MinStack:
    def __init__(self):
        self.stack = []
        self.min_list = []


    def push(self, item):
        if len(self.min_list) == 0:
            min_list.append(item)

        self.stack.append(item)

    def pop(self):
        if self.stack[-1] == self.min_list[-1]:
             self.min_list.pop()
        return self.stack.pop()

    def min(self):
        return self.min_list[-1]

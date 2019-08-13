class Stack:
    class StackNode:
        def __init__(self, data, next=None):
            self.data = data
            self.next = None

    def __init__(self, top=None):
        self.top = None

    def pop(self):
        item = self.top
        self.top = self.top.next
        return item

    def push(self, item):
        new_top = new StackNode(item)
        if self.top:
            self.top = new_top
            new_top.next = self.top
        else:
            self.top = new_top

    def peek(self):
        return self.top

    def isEmpty(self):
        if self.top is None:
            return True

        else:
            return False

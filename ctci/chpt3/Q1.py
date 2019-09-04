class ThreeInOne:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.stack = [0] * (self.numstacks + stacksize)
        self.stacksize = stacksize
        self.sizes = [0] * self.numstacks

    def Pop(self, stack_num):
        if isEmpty(stack_num):
            raise Exception("Stack is empty")
        item = self.stack[self.IndexOfTop(stack_num)]
        self.stack[self.IndexOfTop(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return item

    def Push(self,item,stack_num):
        if isFull(stack_num):
            raise Exeception("Stack is full")
        self.sizes[stack_num] += 1
        self.stack[IndexOfTop(stack_num)] = item

    def Peek(self,stack_num):
        if isEmpty(stack_num):
            raise Exception("Stack is empty")
        return self.stack[self.IndexOfTop(stack_num)]

    def IsEmpty(stack_num):
        return self.sizes[stack_num] == 0

    def IsFull(stack_num):
        return self.sizes[stack_num] == stacksize

    def IndexOfTop(self, stack_num):
        top_index = self.stacksize * stack_num + self.sizes[stack_num] -1
        return top_index



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.value) + " R:" + str(self.right)+')'

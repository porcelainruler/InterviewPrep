from sys import stdin

class Stack:

    def __init__(self):
        super().__init__()
        self.arr = list()
        self.size = 0

    def push(self, data: int):
        self.arr.append(data)
        self.size += 1
    
    def pop(self):
        if self.size <= 0:
            raise Exception('Stack already empty')

        temp = self.arr.pop()
        self.size -= 1
        return temp

    def getSize(self):
        return self.size
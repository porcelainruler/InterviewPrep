from sys import stdin

class Node:
    def __init__(self, data: int):
        super().__init__()
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        super().__init__()
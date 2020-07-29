from sys import stdin

class Node:
    def __init__(self, data: int):
        super().__init__()
        self.data = data
        # self.left = None
        # self.right = None
        self.next = None


class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.size = 0
        self.helper = None

    def addNodeFirst(self, data: int):
        temp = Node(data)
        if not self.head:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp 
        self.size += 1

    def addNodeLast(self, data: int):
        if not self.head:
            temp = Node(data)
            self.head = temp
            self.tail = temp
        else:
            temp = self.tail
            temp.next = Node(data)
            self.tail = temp.next
        
        self.size += 1

    def addNodeAt(self, data: int, index: int):
        if index >= self.size:
            raise Exception('Index out of range')

        if index == 0:
            self.addNodeFirst(data)
        elif index == self.size:
            self.addNodeLast(data)
        else:
            temp = self.head

            count = 0
            while count < index-1:
                temp = temp.next
                count += 1
            nn = Node(data)
            store = temp.next
            temp.next = nn
            nn.next = store

            self.size += 1

        return

    def removeNodeFirst(self):
        temp = self.head

        if not temp:
            raise Exception('Linked list already empty')

        if not temp.next:
            self.head = None
            self.tail = None
            self.size = 0
            return temp
        
        if not temp.next.next:
            store = temp
            self.head = temp.next
            self.size -= 1
            return store

    def removeNodeLast(self):
        temp = self.head

        if not self.head:
            raise Exception('Linked List already Empty')

        if not temp.next:
            store = temp
            self.head = None
            self.tail = None
            self.size = 0
            return temp

        while temp.next.next:
            temp = temp.next 
        
        store = temp.next
        temp.next = None
        self.tail = temp
        self.size -= 1

        return store

    def removeNodeAt(self, index: int):
        if index >= self.size:
            raise Exception('Index out of range')

        if index == 0:
            return self.removeNodeFirst()

        elif index == self.size-1:
            return self.removeNodeLast()

        else:
            temp = self.head
            count = 0

            while count < index-1:
                temp = temp.next 
                count += 1
            
            store = temp.next 
            temp.next = temp.next.next
            self.size -= 1
            return store

    def getSize(self):
        return self.size
            
    def printLL(self):
        temp = self.head

        print('Linked List:', end=' ')
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        
        print()

    def fold(self):
        self.helper = self.head
        
        self.foldh(self.head, 0)

    def foldh(self, head: Node, idx: int):
        if head == None:
            return
        
        self.foldh(head.next, idx+1)

        if idx > self.size//2:
            store = self.helper.next
            self.helper.next = head
            head.next = store
            self.helper = store

        elif idx == self.size//2:
            head.next = None
            self.tail = head

    def midNode(self) -> Node:
        temp1 = self.head
        temp2 = self.head

        while temp2.next != None:
            if temp2.next.next != None:
                temp1 = temp1.next
                temp2 = temp2.next.next

        return temp1

    def kReversal(self, k: int):
        None


def main():
    arr = list(map(int, stdin.readline().split()))

    LL = LinkedList()

    for ele in arr:
        LL.addNodeLast(ele)
    
    LL.printLL()
    # LL.removeNode()
    # LL.addNodeAt(20, 2)
    # LL.printLL()
    # print('Size: ', LL.getSize())
    # LL.removeNodeAt(3)
    # LL.printLL()
    # LL.fold()
    # LL.printLL()
    print(LL.midNode().data)




if __name__ == '__main__':
    main()
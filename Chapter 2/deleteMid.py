class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        head = self.head
        if(head is None):
            self.head = newNode
            return
        current = head
        while(current.next):
            current = current.next
        newNode.next = current.next
        current.next = newNode
    
    def deleteMid(self):
        head = self.head
        count = 0
        current = head
        while(current.next):
            current = current.next
            count += 1 
        mid = 0
        current = head
        while(mid < (count // 2)-1):
            current = current.next
            mid += 1
        next = current.next.next
        current.next = next
        current = current.next

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

def main():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.insert(7)
    LL.insert(8)
    LL.deleteMid()
    LL.printLL()
main()
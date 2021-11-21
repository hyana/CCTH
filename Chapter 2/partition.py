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
    
    def partition(self, k):
        current = self.head
        head = current
        tail = head
        while(current.next):
            nextNode = current.next
            if(current.data < k):
                current.next = head
                head = current
            else:
                tail.next = current
                tail = current
            current = nextNode
        tail.next = None
        return tail

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

def main():
    LL = LinkedList()
    LL.insert(5)
    LL.insert(2)
    LL.insert(3)
    LL.insert(7)
    LL.insert(8)
    LL.insert(6)
    LL.insert(1)
    LL.insert(4)
    LL.partition(5)
    LL.printLL()
main()
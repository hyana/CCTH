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

    def deleteFront(self):
        if(self.head.next is None):
            self.head = None
            return
        if(self.head is None):
            return
        if(self.head.next):
            nextNode = self.head.next
            self.head = None
            self.head = nextNode
    
    def deleteDup(self):
        current = self.head
        #needs two pointers
        while(current):
            dup = current
            while(dup.next):
                if(current.data == dup.next.data):
                    dup.next = dup.next.next
                else:
                    dup = dup.next 
            current = current.next

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


def main():
    LL = LinkedList()
    LL.insert(10)
    LL.insert(5)
    LL.insert(4)
    LL.insert(3)
    LL.insert(5)
    LL.insert(5)
    LL.insert(5)
    LL.insert(5)
    LL.deleteDup()
    LL.printLL()
main()
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
    
    def partition(self, x):
        current = self.head
        lroot = left = LinkedList()
        rroot = right = LinkedList()
        while(current):
            if(current.data < x):
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next
            current = current.next
        right.next = None
        left.next = rroot.next
        while(lroot.next):
            print(lroot.next.data)
            lroot = lroot.next

        #because 0 is saved at first when we first made the linkedlists


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
main()
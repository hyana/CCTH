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

    def head(self):
        return self.head

    def ktolast(self, node, ord):
        if node is None:
            return 0
        count = self.ktolast(node.next, ord) + 1
        if count == ord:
            print(node.data)
        return count


    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


def main():
    LL = LinkedList()
    LL.insert(4)
    LL.insert(3)
    LL.insert(5)
    LL.insert(5)
    node = LL.ktolast(LL.head, 2)
main()
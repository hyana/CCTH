class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insertToEmptyList(self, data):
        if(self.start_node is None):
            new_node = Node(data)
            self.start_node = new_node
            return

    def insertToStart(self, data):
        if(self.start_node is None):
            new_node = Node(data)
            self.start_node = new_node
            return
        second = self.start_node
        self.start_node = Node(data)
        self.start_node.next = second 
        second.prev = self.start_node
        
    def insertToEnd(self, data):
        if(self.start_node is None):
            new_node = Node(data)
            self.start_node = new_node 
            return
        n = self.start_node
        while(n.next):
            n = n.next
        new_node = Node(data)
        n.next= new_node
        new_node.prev = n

    def deleteAtStart(self):
        if(self.start_node is None):
            return
        if(self.start_node.next is None):
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def deleteAtEnd(self):
        if(self.start_node.next is None):
            self.start_node = None
            return
        if(self.start_node is None):
            return
        n = self.start_node
        while(n.next):
            n = n.next
        # unless n.prev is non-Null
        n.prev.next = None
    
    def display(self):
        if(self.start_node is None):
            return
        n = self.start_node
        while(n.next):
            print(n.data)
            n = n.next
        print(n.data)
        
    def printLL(self):
        current = self.start_node
        while(current):
            print(current.data)
            current = current.next


def main():
    LL = doublyLinkedList()
    LL.insertToEmptyList(3)
    LL.insertToStart(5)
    LL.insertToStart(1)
    LL.insertToStart(2)
    #LL.insertToEnd(1)
   # LL.deleteAtStart()
    LL.display()
main()
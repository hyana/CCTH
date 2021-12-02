class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.data = Node.self.data
        self.next = Node.next

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

    #brute force solution
    def sum(self, L1, L2):
        first_cur = L1.head
        second_cur = L2.head
        first_str = str()
        second_str = str()
        while(first_cur):
            first_str +=str(first_cur.data)
            first_cur = first_cur.next
        first = int(first_str)
        while(second_cur):
            second_str +=str(second_cur.data)
            second_cur = second_cur.next
        second = int(second_str)
        output = first + second 
        lstr = list(str(output))
        output = LinkedList()
        for s in reversed(lstr):
            output.insert(s)
        output.next = None
        current = output.head
        while(current):
            print(current.data)
            current= current.next

def sum_better(l1, l2):
    sumList = Node(None)
    cur = sumList
    carryOver = False
    while l1 or l2 or carryOver:
        n = Node(None)
        if l1:
            n.data += l1.data
            l1 = l1.next
        if l2:
            n.data += l2.data
            l2 = l2.next
        if carryOver:
            n.data += 1
            carryOver = False
        if n.data > 9:
            carryOver = True
            n.data -= 10
        cur.next = n
        cur = cur.next
    current = sumList.head
    while(current.next):
        print(current.data)
        current = current.next

def main():
    L1 = LinkedList()
    L2 = LinkedList()
    L1.insert(1)
    L1.insert(2)
    L1.insert(3)
    L1.insert(4)
    L2.insert(5)
    L2.insert(6)
    L2.insert(7)
    L2.insert(8)
    sum_better(L1, L2)
    
main()
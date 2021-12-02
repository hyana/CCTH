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
    
    def isPalindrome(self, head):
        self.front = head
        def palindromeCheck(current = head):    
            if current is not None:
                if palindromeCheck(current.next) == False:
                    return False
                if self.front.data != current.data:
                    return False
                self.front = self.front.data
            return True
        return palindromeCheck()

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
    LL.isPalindrome(None)
main()
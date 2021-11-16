class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def main():
    first = Node(4)
    print(first.data)
main()
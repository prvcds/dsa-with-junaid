# Linked List using Loops

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListLoop:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:   # loop
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    ll = LinkedListLoop()
    for i in [1, 2, 3, 4]:
        ll.insert(i)

    print("Loop-based traversal:")
    ll.print_list()

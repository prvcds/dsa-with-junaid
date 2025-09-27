# Linked List using Recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListRecursion:
    def __init__(self):
        self.head = None

    def insert(self, data):
        def _insert(node, data):
            if not node:
                return Node(data)
            node.next = _insert(node.next, data)
            return node
        self.head = _insert(self.head, data)

    def print_list(self, node=None):
        if node is None:
            node = self.head
        if not node:
            print("None")
            return
        print(node.data, end=" -> ")
        self.print_list(node.next)


if __name__ == "__main__":
    ll = LinkedListRecursion()
    for i in [10, 20, 30, 40]:
        ll.insert(i)

    print("Recursion-based traversal:")
    ll.print_list()

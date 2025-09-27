# Linked List with Single Int Variable for Counting

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListCount:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def count_nodes(self):
        count = 0  # single int variable
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


if __name__ == "__main__":
    ll = LinkedListCount()
    for i in [100, 200, 300, 400, 500]:
        ll.insert(i)

    print("Count using single int variable:", ll.count_nodes())

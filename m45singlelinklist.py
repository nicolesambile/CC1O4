class Node:
    def __init__(self, data):
        self.data_nbs = data
        self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head_nbs = None

        def insert_at_head(self, data):
            new_node = Node(data)
            new_node.next = self.head_nbs
            self.head_nbs = new_node

        def insert_at_end (self, data):
            new_node = Node(data)
            if not self.head_nbs:
                self.head_nbs = new_node
                return
            current = self.head_nbs
            while current.next:
                current = current.next
                current.next = new_node

        def traverse(self):
            current = self.head
            while current:
                print(current.data, end=" -> ")
                print("None")

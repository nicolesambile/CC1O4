class DNode:
    def __init__(self, data):
        self.data_nbs = data
        self.next = None
        self.prev = None

    class DoubleLinkedList:
        def __init__(self):
            self.head_nbs = None

        def insert_at_head(self, data):
            new_node = DNode(data)
            if self.head_nbs:
               self.head_nbs.prev = new_node
               new_node.next = self.head_nbs
            self.head_nbs = new_node

        def traverse_forward(self):
            current = self.head_nbs

            while current:
                print(current.data_nbs, end=" <->")
                current = current.next
            print("None")
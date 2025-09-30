class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
     def __init__(self):
         self.head_nbs = None

     def insert(self, data):
         new_node = CNode(data)
         if not self.head_nbs:
             self.head_nbs = new_node

             new_node.next = self.head_nbs
             return
         current = self.head_nbs
         while current.next != self.head_nbs:
             current = current.next
         current.next = new_node
         new_node.next = self.head_nbs

     def traverse(self):
         if not self.head_nbs:
             return
         current = self.head_nbs
         while True:
             print(current.data, end=" -> ")
             current = current.next
             if current == self.head_nbs:
                 break
         print("(back to head)")
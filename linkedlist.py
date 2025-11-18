class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes (Clues)
head_ss = Node("Clue 1")
head_ss.next = Node("Clue 2")
head_ss.next.next = Node("Clue 3")

# Traversing
current_ss = head_ss
while current_ss:
    print(current_ss.data)
    current_ss = current_ss.next

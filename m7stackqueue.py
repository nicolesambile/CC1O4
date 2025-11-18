stack_nbs = []
stack_nbs.append(10) 
stack_nbs.append(20)
print(stack_nbs.pop())

from collections import deque
queue_nbs = deque()
queue_nbs.append(10) 
queue_nbs.append(20)
print(queue_nbs.popleft()) 
print("last queue:", queue_nbs)
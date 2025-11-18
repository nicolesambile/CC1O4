from collections import deque
queue_ss = deque()

#People join line
queue_ss.append ("Alice")
queue_ss.append ("Bob")
queue_ss.append ("Donny")
queue_ss.append ("Belle")

#Serve first person
print(queue_ss.popleft())
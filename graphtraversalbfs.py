from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

def bfs_ss(start):
    visited_ss = set() 
    queue = deque([start])

    while queue:
        vertex_ss = queue.popleft()
        if vertex_ss not in visited_ss:
            print(vertex_ss, end=" ")
            visited_ss.add(vertex_ss)
            queue.extend(graph[vertex_ss])  

bfs_ss("A")

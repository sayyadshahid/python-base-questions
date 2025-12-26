# ===============================
# DFS USING STACK (ITERATIVE)
# ===============================

graph = {
    'A': ['C', 'B'],
    'B': ['E', 'D'],
    'C': [],
    'D': [],
    'E': []
}

visited = set()
stack = ['A']

while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        stack.extend(graph[node])

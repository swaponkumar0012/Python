# ----------------------------
# Adjacency Matrix Graph + DFS
# ----------------------------

# Example graph (undirected):
# 0 -- 1 -- 2
# |    |
# 3 -- 4
# Represented as an adjacency matrix:

graph = [
    [0, 1, 0, 1, 0],  # 0 connected to 1, 3
    [1, 0, 1, 0, 1],  # 1 connected to 0, 2, 4
    [0, 1, 0, 0, 0],  # 2 connected to 1
    [1, 0, 0, 0, 1],  # 3 connected to 0, 4
    [0, 1, 0, 1, 0]   # 4 connected to 1, 3
]

n = len(graph)
visited = [False] * n

def dfs(vertex):
    """Depth-First Search starting from given vertex."""
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbor in range(n):
        if graph[vertex][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor)

# Run DFS from vertex 0:
print("DFS traversal starting from vertex 0:")
dfs(0)

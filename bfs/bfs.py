from collections import deque


def bfs(graph, start_node):
    queue = deque([start_node])
    visited = set()
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


graph = {
    0: [1, 2, 3],
    1: [],
    2: [4],
    3: [5],
    4: [],
    5: []
}

# Start BFS from node 0
bfs(graph, 0)

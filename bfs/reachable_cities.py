from collections import defaultdict, deque


def reachable_cities(n, m, fuel, start_city, edges):
    # Build adjacency list for the graph
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque([(start_city, fuel)])
    visited = set()
    while queue:
        city, remaining_fuel = queue.popleft()
        if city in visited:
            continue
        visited.add(city)
        if remaining_fuel > 0:
            for neighbor in graph[city]:
                if neighbor not in visited:
                    queue.append((neighbor, remaining_fuel - 1))
    return len(visited)


n = 6
m = 5
fuel = 2
start_city = 1
edges = [(2, 5), (1, 5), (3, 4), (2, 4), (5, 3)]

# Call the modified function
result = reachable_cities(n, m, fuel, start_city, edges)
print(result)

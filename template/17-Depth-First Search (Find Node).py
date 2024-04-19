def dfs(n, graph, start):
    adjacent = [[] for _ in range(n + 1)]

    for a, b in graph:
        adjacent[a].append(b)
        adjacent[b].append(a)

    visited = []
    queue = [start]

    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            queue.extend(adjacent[node])

    return visited


n = 11
graph = [
    [1, 2],
    [1, 3],
    [1, 8],
    [2, 6],
    [2, 10],
    [3, 5],
    [3, 4],
    [3, 9],
    [4, 7],
    [9, 11],
]

print(dfs(n, graph, 1))

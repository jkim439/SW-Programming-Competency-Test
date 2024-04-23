from heapq import *


def dijkstra(n, graph, start):
    adjacent = [[] for _ in range(n + 1)]
    for a, b, d in graph:
        adjacent[a].append([d, b])
        adjacent[b].append([d, a])

    distances = [float("inf")] * (n + 1)
    distances[start] = 0

    queue = []
    heappush(queue, [0, start])

    while queue:
        cost, node = heappop(queue)

        for c, n in adjacent[node]:
            if cost + c < distances[n]:
                distances[n] = cost + c
                heappush(queue, [cost + c, n])

    return distances


n = 5
graph = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]

print(dijkstra(n, graph, 5))

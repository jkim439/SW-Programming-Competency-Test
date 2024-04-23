from heapq import *


def prim(n, graph, start):
    mst = []

    adjacent = [[] for _ in range(n + 1)]
    for a, b, w in graph:
        adjacent[a].append([w, a, b])
        adjacent[b].append([w, b, a])

    visited = {start}
    queue = adjacent[start]
    heapify(queue)

    while queue:
        w, a, b = heappop(queue)

        if b not in visited:
            visited.add(b)
            mst.append([a, b, w])

            for edge in adjacent[b]:
                if edge[2] not in visited:
                    heappush(queue, edge)
    return mst


n = 7
graph = [
    [1, 2, 7],
    [1, 4, 5],
    [2, 1, 7],
    [2, 3, 8],
    [2, 4, 9],
    [2, 5, 7],
    [3, 2, 8],
    [3, 5, 5],
    [4, 1, 5],
    [4, 2, 9],
    [4, 5, 7],
    [4, 6, 6],
    [5, 2, 7],
    [5, 3, 5],
    [5, 4, 7],
    [5, 6, 8],
    [5, 7, 9],
    [6, 4, 6],
    [6, 5, 8],
    [6, 7, 11],
    [7, 5, 9],
    [7, 6, 11],
]

print(prim(n, graph, 1))

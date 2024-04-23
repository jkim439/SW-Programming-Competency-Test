parent, rank = {}, {}


def kruskal(graph):
    mst = []

    for node in set([i[0] for i in graph]):
        parent[node] = node
        rank[node] = 0

    for edge in sorted(graph, key=lambda x: x[2]):
        a, b, _ = edge
        if find(a) != find(b):
            union(a, b)
            mst.append(edge)

    return mst


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    root1, root2 = find(a), find(b)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        rank[root2] += 1
        parent[root1] = root2


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

print(kruskal(graph))

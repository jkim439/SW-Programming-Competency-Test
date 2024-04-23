def bfs(r, c, graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[0] * (c + 1) for _ in range(r + 1)]
    visited[0][0] = 1
    queue = [[0, 0]]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if (
                0 <= ny <= r
                and 0 <= nx <= c
                and visited[ny][nx] == 0
                and graph[ny][nx] == 1
            ):
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    return visited[r][c]


print(
    bfs(
        3,
        5,
        [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
        ],
    )
)

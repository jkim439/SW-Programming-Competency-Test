def dfs(r, c, y, x, graph):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if (
            0 <= ny <= r
            and 0 <= nx <= c
            and visited[ny][nx] == 0
            and graph[ny][nx] == 1
        ):
            visited[ny][nx] = visited[y][x] + 1
            dfs(r, c, ny, nx, graph)

    return visited[r][c]


r = 3
c = 5
visited = [[0] * (c + 1) for _ in range(r + 1)]
visited[0][0] = 1


print(
    dfs(
        3,
        5,
        0,
        0,
        [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
        ],
    )
)

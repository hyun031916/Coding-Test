from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
que = deque()
que.append((0, 0))
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]


def bfs():
    while que:
        node_x, node_y = que.popleft()
        for i in range(4):
            nx = node_x + x[i]
            ny = node_y + y[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] += graph[node_x][node_y]
                que.append((nx, ny))


bfs()
print(graph[n - 1][n - 1])

MAP = [list(map(int, input.split())) for _ in range(int(input()))]

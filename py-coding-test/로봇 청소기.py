dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board[x][y] = 2


# def clean(x, y, d):
#     global ans
#     if a[x][y] == 0:
#         a[x][y] = 2
#         ans += 1
#     for _ in range(4):
#         nd = (d+3)%4
#         nx = x +dx[nd]
#         ny = y + dy[nd]
#         if a[nx][ny] == 0:
#             clean(nx, ny, nd)
#             return
#         d = nd
#     nd = (d+2)%4
#     nx = x+dx[nd]
#     ny = y+dy[nd]
#     if a[nx][ny] == 1:
#         return
#     clean(nx, ny, d)

def solve(x, y, d, answer):
    while True:
        check = False
        for k in range(4):
            nd = (d+3)%4
            next_x, next_y = x+dx[nd], y+dy[nd]
            d = nd
            if not board[next_x][next_y]:
                board[next_x][next_y] = 2
                answer += 1
                x, y = next_x, next_y
                check = True
                break
        if not check:
            if board[x- dx[d]][y-dy[d]] == 1:
                return answer
            else:
                x, y = x - dx[d], y - dy[d]

print(solve(x, y, d, 1))
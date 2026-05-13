import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())

grid = []
for i in range(H):
    row = list(input().strip())
    grid.append(row)

    for j, c in enumerate(row):
        if c == 'S':
            sy, sx = i, j
        if c == 'G':
            gy, gx = i, j

DIR = [(-1,0),(1,0),(0,-1),(0,1)]

# visited[y][x][parity]
visited = [[[False]*2 for _ in range(W)] for _ in range(H)]

q = deque()
q.append((sy, sx, 0, 0))
visited[sy][sx][0] = True

while q:
    y, x, parity, dist = q.popleft()

    if (y, x) == (gy, gx):
        print(dist)
        exit()

    for dy, dx in DIR:
        ny = y + dy
        nx = x + dx

        if not (0 <= ny < H and 0 <= nx < W):
            continue

        cell = grid[ny][nx]

        # 壁
        if cell == '#':
            continue

        # ドア判定
        if cell == 'o' and parity == 1:
            continue

        if cell == 'x' and parity == 0:
            continue

        nparity = parity

        # スイッチ踏んだら反転
        if cell == '?':
            nparity ^= 1

        if visited[ny][nx][nparity]:
            continue

        visited[ny][nx][nparity] = True
        q.append((ny, nx, nparity, dist + 1))

print(-1)

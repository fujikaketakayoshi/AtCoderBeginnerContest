import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# print(H, W)

grid = []
for _ in range(H):
  row = list(input().strip())
  grid.append(row)
# print(grid)

A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1
# print(A,B,C,D)

dist = [[0] * W for _ in range(H)]
# print(visited)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

INF = 10**18
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0

q = deque([(A, B)])

while q:
    y, x = q.popleft()
    for dy, dx in DIRS:
        # 隣
        ny = y + dy
        nx = x + dx
        if 0 <= ny < H and 0 <= nx < W:
            # 道ならコスト0
            if grid[ny][nx] == '.' and dist[ny][nx] > dist[y][x]:
                dist[ny][nx] = dist[y][x]
                q.appendleft((ny, nx))
            # 前蹴りで1マス先
            if dist[ny][nx] > dist[y][x] + 1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
        # 2マス先
        ny2 = y + dy * 2
        nx2 = x + dx * 2
        if 0 <= ny2 < H and 0 <= nx2 < W:
            if dist[ny2][nx2] > dist[y][x] + 1:
                dist[ny2][nx2] = dist[y][x] + 1
                q.append((ny2, nx2))
print(dist[C][D])
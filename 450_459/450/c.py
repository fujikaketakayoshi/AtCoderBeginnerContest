import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# print(H, W)

grid = []
for _ in range(H):
  grid.append(list(input().strip()))
# print(grid)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * W for _ in range(H)]
# print(visited)

def bfs(sy, sx):
  q = deque()
  q.append((sy, sx))
  visited[sy][sx] = True
  while q:
    y, x = q.popleft()
    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]
      if not (0 <= ny <= H - 1 and 0 <= nx <= W - 1):
        continue
      if grid[ny][nx] == '#' or visited[ny][nx]:
        continue
      q.append((ny, nx))
      visited[ny][nx] = True

for y in [0, H - 1]:
  for x in range(W):
    if grid[y][x] == '#' or visited[y][x]:
      continue
    bfs(y,x)

for x in [0, W - 1]:
  for y in range(H):
    if grid[y][x] == '#' or visited[y][x]:
      continue
    bfs(y, x)

cnt = 0
for y in range(1, H - 1):
  for x in range(1, W - 1):
    if grid[y][x] == '#' or visited[y][x]:
      continue
    else:
      bfs(y, x)
      cnt += 1

print(cnt)
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# print(H, W)
a
grid = []
Es = []
visited = [[False] * W for _ in range(H)]
for h in range(H):
  row = list(input().strip())
  grid.append(row)
  for w, r in enumerate(row):
    if r == 'E':
      Es.append((h, w))
      visited[h][w] = True
ans = grid[:]
# print(grid)
# print(Es)
# print(visited)

DIRS = [(-1, 0, 'v'), (0, 1, '<'), (1, 0, '^'), (0, -1, '>')]


q = deque()
q.extend(Es)
# print(q)

while q:
  y, x = q.popleft()
  for dy, dx, dd in DIRS:
    ny = dy + y
    nx = dx + x
    if not(0 <= ny < H and 0 <= nx < W):
      continue
    if visited[ny][nx] or grid[ny][nx] == '#':
      continue
    ans[ny][nx] = dd
    visited[ny][nx] = True
    q.append((ny, nx))

for row in ans:
  print(''.join(row))


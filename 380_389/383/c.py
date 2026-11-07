import sys
input = sys.stdin.readline
from collections import deque

H, W, D = map(int, input().split())
# print(H, W, D)

grid = []
hs = []
for h in range(H):
  S = input().strip()
  grid.append(S)
  for w, s in enumerate(S):
    if s == 'H':
      hs.append((h, w))
# print(grid)
# print(hs)


cnt = [[-1] * W for _ in range(H)]
for y, x in hs:
  cnt[y][x] = 0
# print(cnt)

q = deque()
q.extend(hs)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = len(hs)

while q:
  y, x = q.popleft()
  c = cnt[y][x]
  if c == D:
    continue
  for dy, dx in DIRS:
    ny = y + dy
    nx = x + dx
    if not (0 <= ny < H and 0 <= nx < W):
      continue
    if grid[ny][nx] == '#':
      continue
    if cnt[ny][nx] != -1:
      continue
    cnt[ny][nx] = c + 1
    ans += 1
    q.append((ny, nx))

print(ans)
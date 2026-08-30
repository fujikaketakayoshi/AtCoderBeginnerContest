import sys
input = sys.stdin.readline
from collections import deque

H, W, K = map(int, input().split())
# print(H, W, K)

grid = []
Hb = [False] * H
Wb = [False] * W
for h in range(H):
  srow = input().strip()
  if '#' in srow:
    Hb[h] = True
  row = list(srow)
  for w, r in enumerate(row):
    if r == '#':
      Wb[w] = True
  grid.append(row)

# print(grid, Hb, Wb)

secure = []
for h in range(H):
  for w in range(W):
    if not Hb[h] and not Wb[w]:
      secure.append((h, w))
# print(secure)

q = deque()
for h, w in secure:
  q.append((h, w, 0))
# print(q)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = set(secure)
while q:
  h, w, c = q.popleft()
  if c < K:
    for dy, dx in DIRS:
      ny = dy + h
      nx = dx + w
      if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#' or (ny, nx) in ans:
        continue
      ans.add((ny, nx))
      q.append((ny, nx, c + 1))

print(len(ans))
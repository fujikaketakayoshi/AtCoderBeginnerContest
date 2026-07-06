import sys
input = sys.stdin.readline
import math
from collections import deque

H, W = map(int, input().split())
print(H, W)

grid = []
irmaxs = []
irmax = float('-INF')
for h in range(H):
  row = []
  
  for w, r in enumerate(list(map(int, input().split()))):
    ir = math.isqrt(r)
    if ir == irmax:
      irmaxs.append((h, w))
    elif ir > irmax:
      irmax = ir
      irmaxs = [(h, w)]
    row.append(ir)
  grid.append(row)
print(grid)
print(irmaxs)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

irs = set()
irs_max = float('-INF')
def dfs(h, w, xorsum):
  global irs_max
  ir = grid[h][w]
  xorsum ^= ir ** 2
  irs.add(ir)
  print(h, w, irs)
  irs_max = max(irs_max, xorsum)
  for dy, dx in DIRS:
    ny = dy + h
    nx = dx + w
    if not (0 <= ny < H and 0 <= nx < W):
      continue
    if grid[ny][nx] in irs:
      continue
    dfs(ny, nx, xorsum)
    irs.remove(grid[ny][nx])
  return

for h, w in irmaxs:
  dfs(h, w, 0)
print(irs_max)

print(10 ^ 7 ^ 2 ^ 0)
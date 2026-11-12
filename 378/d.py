import sys
input = sys.stdin.readline
from collections import deque

H, W, K = map(int, input().split())
# print(H, W, K)

grid = []
for _ in range(H):
  S = input().strip()
  grid.append(S)

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(sy, sx, c):
  if c == K:
    return 1
  cnt = 0
  for dy, dx in DIRS:
    ny = dy + sy
    nx = dx + sx
    if not(0 <= ny < H and 0 <= nx < W):
      continue
    if grid[ny][nx] == '#' or visited[ny][nx]:
      continue
    visited[ny][nx] = True
    cnt += dfs(ny, nx, c + 1)
    visited[ny][nx] = False
  return cnt

ans = 0
for h in range(H):
  for w in range(W):
    visited = [[False] * W for _ in range(H)]
    if grid[h][w] == '#':
      continue
    visited[h][w] = True
    ans += dfs(h, w, 0)
print(ans)
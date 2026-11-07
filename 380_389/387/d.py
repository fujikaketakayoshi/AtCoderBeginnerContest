import sys
input = sys.stdin.readline

H, W = map(int, input().split())
# print(H, W)

grid = []
for h in range(H):
  S = list(input().strip())
  for w, g in enumerate(S):
    if g == 'S':
      start = (h, w)
    elif g == 'G':
      goal = (h, w)
  grid.append(S)
# print(start, goal, grid)

DIRS = {
  'h':[[-1, 0], [1, 0]],
  'v':[[0, 1], [0, -1]]}

ans = []
def dfs(y, x, pre, cnt):
  if (y, x) == goal:
    ans.append(cnt)
    return
  for dy, dx in DIRS[pre]:
    ny = y + dy
    nx = x + dx
    if not(0 <= ny < H and 0 <= nx < W):
      continue
    if grid[ny][nx] == '#' or visited[ny][nx]:
      continue
    now = 'h' if pre == 'v' else 'v'
    visited[ny][nx] = True
    dfs(ny, nx, now, cnt + 1)
    visited[ny][nx] = False

visited = [[False] * W for _ in range(H)]
visited[start[0]][start[1]] = True
dfs(start[0], start[1], 'v', 0)

visited = [[False] * W for _ in range(H)]
visited[start[0]][start[1]] = True
dfs(start[0], start[1], 'h', 0)

print(min(ans) if ans else -1)
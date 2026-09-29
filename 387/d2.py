import sys
input = sys.stdin.readline
from collections import deque

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

visited = [[{'h': False, 'v': False} for _ in range(W)] for _ in range(H)]
# print(visited)

visited[start[0]][start[1]]['h'] = True
visited[start[0]][start[1]]['v'] = True
# print(visited)


q = deque()
q.append((start[0], start[1], 'v', 0))
q.append((start[0], start[1], 'h', 0))
while q:
  y, x, pre, cnt = q.popleft()
  # print(y,x,pre,cnt)
  if (y, x) == goal:
    print(cnt)
    exit()
  for dy, dx in DIRS[pre]:
    ny = y + dy
    nx = x + dx
    if not(0 <= ny < H and 0 <= nx < W):
      continue
    now = 'h' if pre == 'v' else 'v'
    if grid[ny][nx] == '#' or visited[ny][nx][now]:
      continue
    visited[ny][nx][now] = True
    q.append((ny, nx, now, cnt + 1))

print(-1)

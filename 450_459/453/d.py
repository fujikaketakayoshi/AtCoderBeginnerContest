import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
MAX = 5 * (10 ** 6)
grid = []
start = ()
goal = ()
for h in range(H):
  row = list(input().strip())
  grid.append(row)
  for i, r in enumerate(row):
    if r == 'S':
      start = (h, i)
    elif r == 'G':
      goal = (h, i)

visited = [[False] * W for _ in range(H)]

dir = {
  'U': (-1, 0),
  'R': (0, 1),
  'D': (1, 0),
  'L': (0, -1),
}

q = deque()
q.append((start[0], start[1], []))
visited[start[0]][start[1]] = True
ans = ''
while q:
  y, x, route = q.popleft()
  # print(y, x, route)
  # if len(route) >= MAX:
  #   break
  if grid[y][x] == 'G':
    ans = route
    break
  if grid[y][x] == 'o':
    key = route[-1]
    dy, dx = dir[key]
    ny = y + dy
    nx = x + dx
    # print('!', ny, nx, route[-1])
    if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#' or visited[ny][nx]:
      continue
    route.append(key)
    q.append((ny, nx, route))
  elif grid[y][x] == 'x':
    keys = list(dir.keys())
    keys.remove(route[-1])
    for d in keys:
      dy, dx = dir[d]
      ny = y + dy
      nx = x + dx
      if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#' or visited[ny][nx]:
        continue
      route.append(d)
      q.append((ny, nx, route))
  else:
    for d, (dy, dx) in dir.items():
      ny = y + dy
      nx = x + dx
      if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#' or visited[ny][nx]:
        continue
      if grid[ny][nx] == '.' or grid[ny][nx] == 'x':
        visited[ny][nx] = True
      route.append(d)
      q.append((ny, nx, route))

if ans != '':
  print('Yes')
  print(''.join(ans))
else:
  print('No')
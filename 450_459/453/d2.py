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

visited = [
    [{'U': False, 'R': False, 'D': False, 'L': False} for _ in range(W)]
    for _ in range(H)
]

dir = {
  'U': (-1, 0),
  'R': (0, 1),
  'D': (1, 0),
  'L': (0, -1),
}
DIR = ['U', 'R', 'D', 'L']

parent = {}

sy, sx = start
q = deque()
for d in dir.keys():
  q.append((sy, sx, d, 0))
  visited[sy][sx][d] = True
goal_state = None
while q:
  y, x, last, cnt = q.popleft()
  # print(y, x, route, visited[y][x])
  if cnt > MAX:
    break
  if grid[y][x] == 'G':
    goal_state = (y, x, last)
    break
  keys = []
  if grid[y][x] == 'o':
    keys = [last]
  elif grid[y][x] == 'x':
    keys = [d for d in DIR if d != last]
  else:
    keys = DIR
  for k in keys:
    dy, dx = dir[k]
    ny = y + dy
    nx = x + dx
    if not (0 <= ny < H and 0 <= nx < W) or grid[ny][nx] == '#' or visited[ny][nx][k]:
      continue
    visited[ny][nx][k] = True
    parent[(ny, nx, k)] = (y, x, last)
    q.append((ny, nx, k, cnt + 1))
if goal_state == None:
  print('No')
  exit()

# 経路復元
path = []
cur = goal_state

while cur in parent:
    y, x, d = cur
    path.append(d)
    cur = parent[cur]

path.reverse()

print("Yes")
print(''.join(path))
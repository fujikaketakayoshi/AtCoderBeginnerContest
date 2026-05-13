import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
# print(H, W)

grid = []
start = ()
goal = ()
for h in range(H):
  row = list(input().strip())
  grid.append(row)
  for i, r in enumerate(row):
    if r == 'S':
      start = (h, i)
    if r == 'G':
      goal = (h, i)
# print(grid)
# print(start, goal)

visited = [[False] * W for _ in range(H)]

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited[start[0]][start[1]] = True

q = deque()
q.append((start[0], start[1], 0, 0, 0))
ans = -1
while q:
  y, x, close_cnt, switch_cnt, cnt = q.popleft()
  # print(y,x,visited)
  if y == goal[0] and x == goal[1]:
    ans = cnt
    break
  if grid[y][x] == '?':
    switch_cnt += 1
  for d in range(4):
    ny = y + DIR[d][0]
    nx = x + DIR[d][1]
    if not (0 <= ny < H and 0 <= nx < W):
      continue
    if (grid[ny][nx] == 'x' and switch_cnt % 2 == 0) or (grid[ny][nx] == 'o' and switch_cnt % 2 == 1):
      close_cnt += 1
      visited[y][x] = close_cnt
      break
  if switch_cnt < close_cnt:
    visited[y][x] = close_cnt
  for d in range(4):
    ny = y + DIR[d][0]
    nx = x + DIR[d][1]
    # print(ny, nx)
    if not (0 <= ny < H and 0 <= nx < W):
      # print('範囲外')
      continue
    if visited[ny][nx] is True or (visited[ny][nx] != False and switch_cnt % 2 != visited[ny][nx]):
      # print(visited[ny][nx] is True, visited[ny][nx] != False and switch_cnt % 2 != visited[ny][nx], '一度通っている')
      continue
    if grid[ny][nx] in ('.', 'G', 'S', '?') or (grid[ny][nx] == 'x' and switch_cnt % 2 == 1) or (grid[ny][nx] == 'o' and switch_cnt % 2 == 0):
      q.append((ny, nx, close_cnt, switch_cnt, cnt + 1))
      visited[ny][nx] = True
print(ans)
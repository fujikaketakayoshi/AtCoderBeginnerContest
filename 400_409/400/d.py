import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
# print(H, W)

grid = []
for _ in range(H):
  row = list(input().strip())
  grid.append(row)
# print(grid)

A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1
# print(A,B,C,D)

visited = [[False] * W for _ in range(H)]
# print(visited)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cntXYs = defaultdict(list)
cnt = 0
for h in range(H):
  for w in range(W):
    if not visited[h][w] and grid[h][w] == '.':
      cnt += 1
      visited[h][w] = cnt
      cntXYs[cnt].append((h, w))
      q = deque()
      q.append((h, w))
      while q:
        y, x = q.popleft()
        for dy, dx in DIRS:
          ny = y + dy
          nx = x + dx
          if not(0 <= ny < H and 0 <= nx < W):
            continue
          if grid[ny][nx] == '#' or visited[ny][nx] > 0:
            continue
          visited[ny][nx] = cnt
          cntXYs[cnt].append((ny, nx))
          q.append((ny, nx))

if cnt == 1:
  print(0)
  exit()

island = [[False] * (cnt + 1) for _ in range(cnt + 1)]
start_cnt = visited[A][B]
goal_cnt = visited[C][D]
# print(visited)
# print(cntXYs)
def dfs(y, x, wcnt, icnt):
  if not(0 <= y < H and 0 <= x < W):
    return
  if visited[y][x] > 0 and visited[y][x] != icnt:
    island[icnt][visited[y][x]] = min(island[icnt][visited[y][x]], wcnt)
    return
  for dy, dx in DIRS:
    ny = y + dy
    nx = x + dx
    ny2 = y + dy * 2
    nx2 = x + dx * 2
    if grid[ny][nx] == '#':
      visited[ny][nx] = True
      dfs(ny, nx, wcnt + 1, icnt)
      visited[ny][nx] = False
    elif grid[ny][nx] == '#' and grid[ny2][nx2] == '#':
      visited[ny][nx] = True
      visited[ny2][nx2] = True
      dfs(ny2, nx2, wcnt + 1, icnt)
      visited[ny][nx] = False
      visited[ny2][nx2] = False


cnts = list(cntXYs.keys())
for k in cnts:
  for h, w in cntXYs[k]:
    dfs(h, w, 0, k)


print(island)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
# print(T)

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRS = 'URDL'

def dfs(y, x, path):
  global ans
  if y == N - 1 and x == N - 1:
    ok = True
    for v in visited:
      if not all(v):
        ok = False
        return False
    ans = path[:]
    return True
  for d in range(4):
    ny = y + DIR[d][0]
    nx = x + DIR[d][1]
    if not (0 <= ny < N and 0 <= nx < N):
      continue
    if visited[ny][nx]:
      continue
    path.append(DIRS[d])
    visited[ny][nx] = True
    # print(ny, nx, path)
    if dfs(ny, nx, path):
      return True
    path.pop()
    visited[ny][nx] = False

for _ in range(T):
  N, A, B = map(int, input().split())
  # print(N,A,B)
  ans = []
  visited = [[False] * N for _ in range(N)]
  # print(visited)
  visited[A - 1][B - 1] = True
  visited[0][0] = True
  dfs(0, 0, [])
  if len(ans) == 0:
    print('No')
  else:
    print('Yes')
    print(''.join(ans))
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# print(N, M)

g = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  g[a].append(b)

q = deque()
q.append((0, 0))
visited = [False] * N
visited[0] = True

while q:
  u, cnt = q.popleft()
  for v in g[u]:
    if v == 0:
      print(cnt + 1)
      exit()
    if visited[v]:
      continue
    q.append((v, cnt + 1))
    visited[v] = True

print(-1)
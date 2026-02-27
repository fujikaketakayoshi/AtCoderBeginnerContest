import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

black = set()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  X, Y = map(int, input().split())
  graph[X].append(Y)
# print(graph)

Q = int(input())
reachable = [set() for _ in range(N + 1)]

for _ in range(Q):
  kind, u = map(int, input().split())
  if kind == 1:
    black.add(u)
  elif kind == 2:
    if not reachable[u]:
      visited = [False] * (N + 1)
      q = deque()
      q.append(u)
      visited[u] = True
      while q:
        v = q.popleft()
        for nv in graph[v]:
          if not visited[nv]:
            reachable[u].add(nv)
            q.append(nv)
            visited[nv] = True
    ok = False
    for b in black:
      if b in reachable[u]:
        print('Yes')
        ok = True
        break
    if not ok:
      print('No')
    

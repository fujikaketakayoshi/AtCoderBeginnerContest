import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# print(N, M)

graph = [set() for _ in range(N)]

for m in range(M):
  U, V, C = map(int, input().split())
  U -= 1
  V -= 1
  graph[U].add((V, C, m))

# print(graph)

q = deque()
q.append((0, 0, None))

while q:
  u, cnt, prec = q.popleft()
  if u == N - 1:
    print(cnt)
    exit()
  lg = list(graph[u])
  for v, c, m in lg:
    if c == prec:
      continue
    q.append((v, cnt + 1, c))
    graph[u].remove((v, c, m))

print(-1)
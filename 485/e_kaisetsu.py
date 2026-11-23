import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# print(N, M)

graph = [[] for _ in range(N)]

for _ in range(M):
  U, V, C = map(int, input().split())
  U -= 1
  V -= 1
  graph[U].append((V, C))

# print(graph)

q = deque()
q.append((0, 0, -1))
first = [-1] * N
second = [False] * N

while q:
  u, cnt, prec = q.popleft()
  if first[u] == -1:
    first[u] = prec
  elif prec == first[u] or second[u]:
    continue
  else:
    second[u] = True
  if u == N - 1:
    print(cnt)
    exit()
  for v, c in graph[u]:
    if c == prec:
      continue
    q.append((v, cnt + 1, c))

print(-1)
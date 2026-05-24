import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
dictgraph = defaultdict(int)

for _ in range(M):
  A, B = map(int, input().split())
  if dictgraph[A] == B:
    continue
  graph[A].append(B)
  dictgraph[A] = B

visited = [False] * (N + 1)
# print(visited)
q = deque()
q.append(1)
visited[1] = True

while q:
  u = q.popleft()
  for v in graph[u]:
    if visited[v]:
      continue
    q.append(v)
    visited[v] = True

cnt = 0
for v in visited:
  if v:
    cnt += 1
print(cnt)

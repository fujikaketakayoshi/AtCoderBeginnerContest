import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# print(N, M)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)

# print(graph)

q = deque()
q.append(1)
visited = [0] * (N + 1)
visited[1] = 1
ans = [[] for _ in range(N + 1)]
cnt = 0
while q:
  u = q.popleft()
  for v in graph[u]:
    if visited[v] == 0:
      1
    elif visited[u] == visited[v]:
      cnt += 1
      continue
    visited[v] = 2 if visited[u] == 1 else 1
    ans[u].append(v)
    q.append(v)
print(cnt)

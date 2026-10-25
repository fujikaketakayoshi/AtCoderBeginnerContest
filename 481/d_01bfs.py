import sys
input = sys.stdin.readline
from collections import deque

N, M, S, T = map(int, input().split())
# print(N, M, S, T)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  # print(A, B)
  graph[A].append(B)

for vs in graph:
  vs.sort()
# print(graph)

dist = [float('inf')] * (N + 1)
dist[S] = 0

q = deque([S])

while q:
    u = q.popleft()

    for i, v in enumerate(graph[u]):
        cost = 0 if i == 0 else 1
        nc = dist[u] + cost

        if nc < dist[v]:
            dist[v] = nc

            if cost == 0:
                q.appendleft(v)
            else:
                q.append(v)

print(-1 if dist[T] == float('inf') else dist[T])

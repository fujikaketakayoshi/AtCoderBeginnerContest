import sys
input = sys.stdin.readline
import heapq

N, M, S, T = map(int, input().split())
# print(N, M, S, T)

graph = [[] for _ in range(N + 1)]
# print(graph)
for _ in range(M):
  A, B = map(int, input().split())
  # print(A, B)
  graph[A].append(B)
# print(graph)

for vs in graph:
  vs.sort()
# print(graph)

hq = [(0, S)]
visited = [False] * (N + 1)
visited[S] = True
while hq:
  c, u = heapq.heappop(hq)
  if u == T:
    print(c)
    exit()
  for i, v in enumerate(graph[u]):
    if visited[v]:
      continue
    if i != 0:
      nc = c + 1
    else:
      nc = c
    heapq.heappush(hq, (nc, v))
    visited[v] = True

print(-1)

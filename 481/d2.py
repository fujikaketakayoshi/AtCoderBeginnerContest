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
dist = [float('inf')] * (N + 1)
dist[S] = 0
ans = float('inf')
while hq:
  c, u = heapq.heappop(hq)
  if u == T:
    ans = min(ans, c)
    continue
  for i, v in enumerate(graph[u]):
    if i != 0:
      nc = c + 1
    else:
      nc = c
    if nc < dist[v]:
      dist[v] = nc
      heapq.heappush(hq, (nc, v))
print(-1 if ans == float('inf') else ans)

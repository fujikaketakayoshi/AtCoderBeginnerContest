import sys
input = sys.stdin.readline
import heapq

N, Q = map(int, input().split())
# print(N, Q)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A, B)

graph = [[] for _ in range(N + 2)]
for i in range(1, N + 1):
  graph[i].append(((i % N) + 1, A[i - 1]))
  graph[(i % N) + 1].append((i, A[i - 1]))
  graph[i].append((N + 1, B[i - 1]))
  graph[N + 1].append((i, B[i - 1]))
# print(graph)

INF = 10 ** 30
dist = [INF] * (N + 2)
start = N + 1
dist[start] = 0

hq = [(0, start)]

while hq:
  d, v = heapq.heappop(hq)
  
  if d != dist[v]:
    continue
  
  for nv, cost in graph[v]:
    nd = d + cost

    if nd < dist[nv]:
      dist[nv] = nd
      heapq.heappush(hq, (nd, nv))
# print(dist)

preA = [0] * (N + 1)
for i in range(1, N + 1):
  preA[i] = preA[i - 1] + A[i - 1]
# print(preA)
Atotal = sum(A)

for _ in range(Q):
  S, T = map(int, input().split())
  # print(S, T)
  if T == N + 1:
    print(dist[S])
  else:
    d = preA[T - 1] - preA[S - 1]
    print(min(dist[S] + dist[T], d, Atotal - d))

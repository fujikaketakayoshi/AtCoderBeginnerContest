import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

graph = [[] for _ in range(N + 1)]
rgraph = [[] for _ in range(N + 1)]
for i in range(N - 1):
  U, V = map(int, input().split())
  graph[U].append(V)
  rgraph[V].append(U)
# print(graph, rgraph)

print('No')
for k in range(2, N + 1):
  aset = set()
  visited = [False] * (N + 1)
  q = deque()
  q.append(1)
  visited[1] = True
  aset.add(A[0])
  ok = False
  while q:
    ok2 = False
    u = q.popleft()
    # print(u, aset)
    for v in graph[u]:
      # print(v, A[v - 1], aset)
      if visited[v]:
        continue
      if A[v - 1] in aset:
        ok2 = True
        break
      if v == k:
        q = deque()
        break
      aset.add(A[v - 1])
      q.append(v)
      visited[v] = True
    if ok2:
      ok = True
      break
    for v in rgraph[u]:
      if visited[v]:
        continue
      if A[v - 1] in aset:
        ok2 = True
        break
      if v == k:
        q = deque()
        break
      aset.add(A[v - 1])
      q.append(v)
      visited[v] = True
    if ok2:
      ok = True
      break
  print('Yes' if ok else 'No')
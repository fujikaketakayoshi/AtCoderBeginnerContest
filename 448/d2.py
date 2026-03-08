import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
# print(N, A)
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
  U, V = map(int, input().split())
  graph[U].append(V)
  graph[V].append(U)
# print(graph)

def dfs(u):
  global cnt
  if u == 1:
    return True if cnt == 1 else False
  for v in graph[u]:
    if visited[v]:
      continue
    if A[v - 1] in Aset:
      visited[v] = True
      cnt += 1
      if dfs(v):
        return True
      cnt -= 1
    else:
      visited[v] = True
      Aset.add(A[v - 1])
      if dfs(v):
        return True
      Aset.remove(A[v - 1])
  return False

print('No')
for k in range(2, N + 1):
  cnt = 0
  Aset = {A[k - 1]}
  visited = [False] * (N + 1)
  dfs(k)
  print('Yes' if cnt == 1 else 'No')
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
# print(N, M)

if N != M:
  print('No')
  exit()

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

# print(graph)

visited = [False] * (N + 1)

def dfs(v, start, cntN):
  for u in graph[v]:
    if u == start and cntN == N:
      print('Yes')
      exit()
    if visited[u]:
      continue
    visited[u] = True
    dfs(u, start, cntN + 1)
    visited[u] = False

visited[1] = True
dfs(1, 1, 1)
print('No')
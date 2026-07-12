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

for v in range(1, N + 1):
  if len(graph[v]) != 2:
    print('No')
    exit()

# print(graph)

visited = [False] * (N + 1)

def dfs(v, start, cntN):
  visited[v] = True
  for u in graph[v]:
    if u == start and cntN == N:
      print('Yes')
      exit()
    if visited[u]:
      continue
    dfs(u, start, cntN + 1)

visited[1] = True
dfs(1, 1, 1)
print('No')
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, w = map(int, input().split())
  graph[u].append((v, w))
  graph[v].append((u, w))

# print(graph)


ans = float('INF')
def dfs(u, xor):
  global ans
  if u == N:
    # print(xor)
    ans = min(ans, xor)
    return
  
  for v, w in graph[u]:
    # print(u, v, w)
    if visited[v]:
      continue
    visited[v] = True
    dfs(v, xor ^ w)
    visited[v] = False

visited = [False] * (N + 1)
visited[1] = True
dfs(1, 0)

print(ans)
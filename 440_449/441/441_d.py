import sys
input = sys.stdin.readline

N, M, L, S, T = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
  U, V, C = map(int, input().split())
  graph[U].append((V, C))

results = set()

def dfs(u, cnt, cost):
  if cost > T:
    return
  if cnt == L:
    if S <= cost <= T:
      results.add(u)
    return
  for (v, c) in graph[u]:
    dfs(v, cnt + 1, cost + c)

dfs(1, 0, 0)

ans = sorted(results)
print(' '.join(map(str, ans)))
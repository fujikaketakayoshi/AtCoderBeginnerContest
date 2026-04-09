import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

T = int(input())
print(T)

def dfs(u, k, path):
  if k == 2 * K:
    results.append((path[:], S[u]))
    return
  for v in graph[u]:
    path.append(v)
    dfs(v, k + 1, path)
    path.pop()


for _ in range(T):
  N, M, K = map(int, input().split())
  S = [''] + list(input().strip())
  print(N, M, K, S)
  graph = [[] for _ in range(N + 1)]
  results = []
  for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
  print(graph)
  dfs(1, 0, [1])
  print(results)

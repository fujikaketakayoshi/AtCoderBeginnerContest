import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

T = int(input())
# print(T)

def dfs(u, k, path):
  if k == 2 * K:
    if u == 1:
      results.append((path[0], S[path[0]]))
    return
  for v in rgraph[u]:
    path.append(v)
    dfs(v, k + 1, path)
    path.pop()


for _ in range(T):
  N, M, K = map(int, input().split())
  S = [''] + list(input().strip())
  # print(N, M, K, S)
  graph = [[] for _ in range(N + 1)]
  rgraph = [[] for _ in range(N + 1)]
  results = []
  for _ in range(M):
    U, V = map(int, input().split())
    graph[U].append(V)
    rgraph[V].append(U)
  # print(graph, rgraph)
  for n in range(1, N + 1):
    dfs(n, 0, [n])
  ans = [0, 0]
  for n, r in results:
    if r == 'A':
      ans[0] += 1
    else:
      ans[1] += 1
  # print(ans)
  if ans[0] > ans[1]:
    print('Alice')
  else:
    print('Bob')
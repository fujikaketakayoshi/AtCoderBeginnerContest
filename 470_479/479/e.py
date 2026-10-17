import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
# print(N)

ans = [sum(range(1, N))] * N
# print(ans)

reg = [0] * N
AB = []
graph = [[] for _ in range(N)]
for _ in range(N - 1):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  graph[A].append(B)
  graph[B].append(A)
  reg[A] += 1
  reg[B] += 1
  AB.append((A, B))
# print(AB)
# print(reg)
# print(graph)

def bfs(u, n):
  nodes = []
  q = deque()
  q.extend(graph[u])
  visited = [False] * N
  visited[n] = True
  while q:
    v = q.popleft()
    if visited[v]:
      continue
    nodes.append(v)
    visited[v] = True
    for nv in graph[v]:
      q.append(nv)
  return nodes

for i, ab in enumerate(AB):
  i += 1
  a, b = ab
  if reg[a] == 1:
    ans[a] -= i
  elif reg[b] == 1:
    ans[b] -= i
  elif reg[a] > reg[b]:
    nodes = bfs(b, a)
    if len(nodes) < (N + 1) // 2:
      for n in nodes:
        ans[n] -= i
    else:
      all_nodes = set(range(N))
      ex_nodes = all_nodes - set(nodes)
      for n in ex_nodes:
        ans[n] -= i
  else:
    nodes = bfs(a, b)
    if len(nodes) < (N + 1) // 2:
      for n in nodes:
        ans[n] -= i
    else:
      all_nodes = set(range(N))
      ex_nodes = all_nodes - set(nodes)
      for n in ex_nodes:
        ans[n] -= i

print(*ans)
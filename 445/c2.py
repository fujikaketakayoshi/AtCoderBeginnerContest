import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
A = list(map(int, input().split()))

indeg = [[] for _ in range(N + 1)]
goals = []

for i, a in enumerate(A):
  indeg[a].append(i + 1)
  if a == i + 1:
    goals.append(i + 1)

ans = [0] * N

for i in goals:
  queue = deque(indeg[i])
  ans[i - 1] = i
  while queue:
    u = queue.pop()
    if u == i:
      continue
    ans[u - 1] = i
    for v in indeg[u]:
      queue.append(v)
print(*ans)

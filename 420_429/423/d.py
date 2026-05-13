import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, K = map(int, input().split())
# print(N, K)

groups = []
for n in range(N):
  A, B, C = map(int, input().split())
  # print(A, B, C)
  groups.append((A, B, C, n))


q = deque()
q.extend(groups)

eatings = [(0, 0, 0, 0)]
heapq.heapify(eatings)  # リストをヒープに変換

eating_num = 0
waitings = []
now = 0
ans = [0] * N
while q or waitings:
  next_time = float('INF')
  # print(waitings)
  if q:
    g = q.popleft()
    next_time = g[0]
  if eatings and next_time >= eatings[0][0]:
    ate = heapq.heappop(eatings)
    now = ate[0]
    eating_num -= ate[1]
    print(eatings, waitings)
    while waitings and eating_num + waitings[0][2] <= K:
      w = heapq.heappop(waitings)
      eating_num += w[2]
      heapq.heappush(eatings, (now + w[1], w[2], w[3]))
      ans[w[3]] = now
  if g:
    if eating_num + g[2] <= K:
      eating_num += g[2]
      heapq.heappush(eatings, (now + g[1], g[2], g[3]))
      ans[g[3]] = now
    else:
      heapq.heappush(waitings, (g[0], g[1], g[2], g[3]))
# print(eatings, now)
for a in ans:
  print(a)

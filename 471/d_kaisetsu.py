import sys
input = sys.stdin.readline
import heapq

Q, V = map(int, input().split())
# print(Q, V)

bats = []
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    t = query[1]
    w = query[2]
    u = w - t
    heapq.heappush(bats, -u)
  else:
    t = query[1]
    if bats:
      high_u = heapq.heappop(bats)
      print(min(V, t + -high_u))
    else:
      print(-1)
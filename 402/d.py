import sys
input = sys.stdin.readline
import math
from collections import deque

N, M = map(int, input().split())
# print(N, M)

AB = set()
for m in range(M):
  A, B = map(int, input().split())
  AB.add((A, B))


if N == 2:
  print(0)
else:
  heikou = 0
  for i in range(1, N + 1):
    heikou_cnt = 0
    lq = deque()
    lq.extend(list(range(1, i + 1)))
    rq = deque()
    rq.extend(list(range(i + 1, N + 1)))
    while len(lq) >= 2:
      l = lq.popleft()
      r = lq.pop()
      if (l, r) in AB:
        heikou_cnt += 1
    while len(rq) >= 2:
      l = rq.popleft()
      r = rq.pop()
      if (l, r) in AB:
        heikou_cnt += 1
    # print(heikou_cnt)
    heikou += math.comb(heikou_cnt, 2)
  # print(heikou)
  print(math.comb(M, 2) - heikou)
import sys
input = sys.stdin.readline
import math
import bisect

T = int(input())
# print(T)

for _ in range(T):
  N = int(input())
  # print(N)
  ts = []
  for _ in range(N):
    X, Y = map(int, input().split())
    t = math.degrees(math.atan2(Y, X))
    # print(X, Y, t)
    ts.append(t)
  ts.sort()
  # print(ts)
  ans = 0
  for i in range(len(ts)):
    if ts[i] < 0:
      base = ts[i] + 180
      idx = bisect.bisect_left(ts, base)
      cnt = idx - i
    else:
      base = ts[i] - 180
      idx = bisect.bisect_left(ts, base)
      cnt = i - idx + 1
    # print(ts[i], base, i, idx, cnt)
    ans = max(ans, cnt, N - cnt)
  print(ans)

#
#
#
#           *
#              *
#------------+------------------
#              *
#
#          *
#
#
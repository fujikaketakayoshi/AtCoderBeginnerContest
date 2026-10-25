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
  ts = sorted(t % 360 for t in ts)
  ts2 = ts + [t + 360 for t in ts]
  # print(ts2)
  
  ans = 0
  for i in range(N):
    j = bisect.bisect_left(ts2, ts[i] + 180, i, i + N)
    ans = max(ans, j - i)
  print(ans)

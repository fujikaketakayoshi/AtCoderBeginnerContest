import sys
input = sys.stdin.readline
import bisect

Q = int(input())

Ts = []
totalT = 0
precnt = 0
for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    Ts.append(totalT)
  elif q[0] == 2:
    T = q[1]
    totalT += T
  else:
    H = q[1]
    
    cnt = bisect.bisect_right(Ts, totalT - H)
    ans = cnt - precnt
    print(ans)
    precnt = cnt

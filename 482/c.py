import sys
input = sys.stdin.readline
from collections import defaultdict
import bisect

H, W, N, Q = map(int, input().split())
# print(H, W, N, Q)

Hcnt = defaultdict(list)
Wcnt = defaultdict(list)

for _ in range(N):
  R, C = map(int, input().split())
  Hcnt[R].append(C)
  Wcnt[C].append(R)
# print(Hcnt)
# print(Wcnt)

Hidx = list(sorted(Hcnt.keys()))
Widx = list(sorted(Wcnt.keys()))
# print(Hidx)
# print(Widx)

preH = [0] * (len(Hidx) + 1)
for h in range(1, len(Hidx) + 1):
  preH[h] = preH[h - 1] + len(Hcnt[Hidx[h - 1]])
# print(preH)

preW = [0] * (len(Widx) + 1)
for w in range(1, len(Widx) + 1):
  preW[w] = preW[w - 1] + len(Wcnt[Widx[w - 1]])
# print(preW)


for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    u, d = query[1], query[2]
    if d in Hcnt:
      didx = bisect.bisect_right(Hidx, d)
      dsum = preH[didx]
    else:
      # print('here')
      didx = bisect.bisect_left(Hidx, d)
      dsum = preH[didx]
    # print(d, didx, dsum)
    if u in Hcnt:
      uidx = bisect.bisect_right(Hidx, u)
      usum = preH[uidx - 1]
    else:
      # print('here')
      uidx = bisect.bisect_left(Hidx, u)
      usum = preH[uidx]
    # print(u, uidx, usum)
    # print(u,d, uidx, didx)
    print(dsum - usum)
  else:
    l, r = query[1], query[2]
    if r in Wcnt:
      ridx = bisect.bisect_right(Widx, r)
      rsum = preW[ridx]
    else:
      # print('here')
      ridx = bisect.bisect_left(Widx, r)
      rsum = preW[ridx]
    # print(r, ridx, rsum)
    if l in Wcnt:
      lidx = bisect.bisect_right(Widx, l)
      lsum = preW[lidx - 1]
    else:
      # print('here')
      lidx = bisect.bisect_left(Widx, l)
      lsum = preW[lidx]
    # print(l, lidx, lsum)
    # print(u,d, uidx, didx)
    print(rsum - lsum)

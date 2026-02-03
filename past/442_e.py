import sys
input = sys.stdin.readline
import math
import bisect

N, Q = map(int, input().split())

mons = []
tmp180 = []
for _ in range(N):
  X, Y = map(int, input().split())
  theta = math.degrees(math.atan2(Y, X))
  mons.append(theta)
sort_mons = sorted(mons)

for _ in range(Q):
  A, B = map(int, input().split())
  A -= 1
  B -= 1
  # print(A, B, mons[A], mons[B])
  if mons[A] >= mons[B]:
    kukan = [(mons[B], mons[A])]
  else:
    kukan = [(-180, mons[A]), (mons[B], 180)]
  
  # print(sort_mons)
  cnt = 0
  for (ks, ke) in kukan:
    idxl = bisect.bisect_left(sort_mons, ks)
    idxr = bisect.bisect_right(sort_mons, ke)
    cnt += idxr - idxl
    # print(ks, ke, idxl, idxr)
  print(cnt)

import sys
input = sys.stdin.readline
import bisect

N = int(input())
# print(N)

AMAX = 41
BMAX = 10 ** 9

Xas = []
for a in range(1, AMAX + 1):
  Xa = 2 ** a
  if Xa > N:
    break
  Xas.append(Xa)
# print(Xas)

cnt = 0
for xa in Xas:
  l = 1
  r = BMAX + 1
  mid = 0
  while l < r:
    mid = (l + r) // 2
    # print('l,r,mid,X', l, r, mid, xa * (mid ** 2))
    if xa * (mid ** 2) > N:
      r = mid - 1
    else:
      l = mid + 1
  idx = bisect.bisect_right(Xas, l)

  print('xa,l,idx', xa, l, idx)
  cnt += l - idx - 1

print(cnt, len(Xas))

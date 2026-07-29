import sys
input = sys.stdin.readline
import bisect

N = int(input())
# print(N)

AMAX = 59
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
  ok = 1
  ng = BMAX + 1
  while ng - ok > 1:
    mid = (ok + ng) // 2
    # print('ok,ng,mid,X', ok, ng, mid, xa * (mid ** 2))
    if xa * mid * mid <= N:
      ok = mid
    else:
      ng = mid
  # print(xa, ok)
  cnt += (ok + 1) // 2

print(cnt)

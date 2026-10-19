import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
# print(N, Q, A)

preA = [0] * (N + 1)
for i in range(N):
  preA[i + 1] = preA[i] + A[i]
# print(preA)

# B = []
# for i in range(N):
#   B += A[0:i + 1]
# print(B)

Bidx = [0]
preB = [0]
for i in range(N):
  Bidx.append(Bidx[i] + (i + 1))
  preB.append(preB[i] + preA[i + 1])
# print(Bidx)
# print(preB)


for _ in range(Q):
  L, R = map(int, input().split())
  # print(L, R)
  BLidx = bisect.bisect_left(Bidx, L)
  BRidx = bisect.bisect_left(Bidx, R)
  # print(BLidx, BRidx)
  base = preB[BRidx - 1] - preB[BLidx]
  # print(base)
  ARidx = Bidx[BRidx] - Bidx[BRidx - 1]
  ARdiff = Bidx[BRidx] - R
  # print(ARidx, ARdiff)
  diffsumAR = preA[ARidx - ARdiff]
  # print(diffsumAR)
  ALidx = Bidx[BLidx] - Bidx[BLidx - 1]
  ALdiff = Bidx[BLidx] - L
  # print(ALidx, ALdiff)
  diffsumAL = preA[ALidx] - preA[ALidx - ALdiff - 1]
  # print(diffsumAL)
  ans = base + diffsumAR + diffsumAL
  print(ans)
  

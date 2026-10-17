import sys
input = sys.stdin.readline
import bisect

N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, M, K)
# print(X, Y)

A.sort()
B.sort()
# print(A, B)

preA = [0]
for i in range(N):
  preA.append(preA[i] + A[i])
# print(preA)

preB = [(0, 0)]
for i in range(M):
  knum = (B[i] + K - 1) // K
  preB.append((preB[i][0] + knum, preB[i][1] + B[i]))
# print(preB)

ans = 0
for bcnt, preBtupple in enumerate(preB):
  ksum, bsum = preBtupple
  if ksum > Y:
    continue
  onenum = X + Y * K - bsum
  idx = bisect.bisect_right(preA, onenum)
  ans = max(ans, bcnt + idx - 1)

print(ans)

import sys
input = sys.stdin.readline
import bisect

MOD = 998244353
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
# print(N, M, A, B)
SA = [0] * (N + 1)
SB = [0] * (M + 1)
for i in range(1, N + 1):
  SA[i] = SA[i - 1] + A[i - 1]
for i in range(1, M + 1):
  SB[i] = SB[i - 1] + B[i - 1]

cnt = 0
for a in A:
  tmp = 0
  idx = bisect.bisect_left(B, a)
  leftsum = SB[idx] - SB[0] if idx > 0 else 0
  rightsum = SB[M] - SB[idx] if idx < len(B) else 0
  # print(a, B, idx, leftsum, rightsum)
  absleft = abs(a * idx - leftsum)
  absright = abs(a * (len(B) - idx) - rightsum)
  cnt += (absleft + absright) % MOD
print(cnt % MOD)

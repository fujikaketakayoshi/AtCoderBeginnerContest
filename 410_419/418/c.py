import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
# print(N,Q)
A = list(map(int, input().split()))
A.sort()
sumA = [0]
total = 0
for a in A:
  total += a
  sumA.append(total)
print(A, sumA)

for _ in range(Q):
  B = int(input())
  if B == 1:
    print(1)
    continue
  idx = bisect.bisect_left(A, B)
  # print(B, idx)
  if idx == len(A):
    if A[-1] == B:
      ans = sumA[-1]
    else:
      ans = -1
  elif sumA[idx - 1] < B:
    ans = sumA[idx - 1] + (len(A) - idx)  * (B - 1) + 1
  else:
    ans = sumA[idx - 1] + B
  print(ans)

import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

# j - A[j] == i + A[i]

B = A[:]
for i in range(N):
  B[i] += i
C = A[:]
for j in range(N):
  C[j] -= j
print(B, C)

cntB = Counter(B)
cntC = Counter(C)

cnt = 0
for k, v in cntB.items():
  cnt += min(cntC[k], v)
print(cnt)
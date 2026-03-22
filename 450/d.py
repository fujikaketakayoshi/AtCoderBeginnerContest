import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(N, K, A)
maxA = A[-1]
# print(maxA)

for i in range(N - 1):
  amari = (maxA - A[i]) % K
  shou = (maxA - A[i]) // K
  A[i] += shou * K
# print(A)

for i in range(N - 1):
  if maxA - A[i] >= A[i] + K - maxA:
    A[i] += K
    maxA = A[i]

print(max(A) - min(A))
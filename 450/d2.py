import sys
input = sys.stdin.readline
from collections import deque

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

q = deque()
q.extend(A)
# print(q)

min_diff = float('INF')
for i in range(N):
  a = q.popleft()
  minA = a
  min_diff = min(min_diff, maxA - minA)
  q.append(a + K)
  maxA = a + K

print(min_diff)

import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
# print(N, M, K, A)

dq = deque()
k = 0
for i in range(N):
  if i + 1 > M:
    k -= dq.popleft()
  if k + A[i] <= K:
    dq.append(A[i])
    k += A[i]
    print('Yes')
  else:
    dq.append(0)
    print('No')
  # print(k, dq)


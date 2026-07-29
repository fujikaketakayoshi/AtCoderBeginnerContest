import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
# print(N, K)
MOD = 10 ** 9

fib = 0
q = deque()
q_sum = 0
for i in range(N + 1):
  if i < K:
    q.append(1)
    q_sum += 1
  else:
    q.append(q_sum)
    f = q.popleft()
    q_sum += (q_sum - f) % MOD
  # print(q, q_sum)
print(q[-1] % MOD)

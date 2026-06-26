import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

A = list(range(1,N + 1))
# print(A)

plus_idx = 0

for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    p = q[1] - 1
    x = q[2]
    idx = (plus_idx + p) % N
    A[idx] = x
  elif q[0] == 2:
    p = q[1] - 1
    idx = (plus_idx + p) % N
    print(A[idx])
  else:
    k = q[1]
    plus_idx = (plus_idx + k) % N

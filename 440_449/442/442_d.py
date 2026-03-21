import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

cumsum = [0] * (N + 1)
for i in range(N):
  cumsum[i + 1] = cumsum[i] + A[i]

for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    x = q[1]
    cumsum[x] = cumsum[x] + A[x] - A[x - 1]
    A[x - 1], A[x] = A[x], A[x - 1]
  elif q[0] == 2:
    l, r = q[1], q[2]
    print(cumsum[r] - cumsum[l - 1])

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
P = list(map(int, input().split()))
# print(N, Q, P)

for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    x = q[1] - 1
    y = q[2] - 1
    P[x], P[y] = P[y], P[x]
  else:
    Pd = [0] * N
    for i, p in enumerate(P):
      Pd[p - 1] = i + 1
    P = Pd[:]
  # print(P)

print(*P)
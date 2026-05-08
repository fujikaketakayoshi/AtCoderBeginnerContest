import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
C = []
for a, b in zip(A, B):
  ans += min(a, b)
  C.append(min(a, b))

for _ in range(Q):
  c, X, V = input().split()
  X = int(X)
  V = int(V)
  i = X - 1
  minV = min(C[i], V)
  ans += minV - C[i]
  C[i] = V
  print(ans)

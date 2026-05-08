import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
# print(N, Q)
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A, B)

ans = 0
for a, b in zip(A, B):
  ans += min(a, b)
# print(ans)

for _ in range(Q):
  c, X, V = input().split()
  X = int(X)
  V = int(V)
  # print(c, X, V)
  i = X - 1
  if c == 'A':
    prev_min = min(A[i], B[i])
    A[i] = V
    now_min = min(A[i], B[i])
    ans += now_min - prev_min
  else:
    prev_min = min(A[i], B[i])
    B[i] = V
    now_min = min(A[i], B[i])
    ans += now_min - prev_min
  print(ans)

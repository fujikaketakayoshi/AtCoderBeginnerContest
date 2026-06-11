import sys
input = sys.stdin.readline
from fractions import Fraction

T = int(input())

for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  # print(N, A)
  C = []
  for a in A:
    C.append((abs(a), a))
  C.sort(reverse=True)
  # print(C)
  ok = True
  r = Fraction(C[0][1], C[-1][1])
  for i in range((N + 2 - 1)// 2):
    if r != Fraction(C[i][1], C[N - i - 1][1]):
      ok = False
      break
#   for i in range(N - 1):
#     if C[1][1] * C[i][1] != C[0][1] * C[i + 1][1]:
#       ok = False
#       break
  print('Yes' if ok else 'No')

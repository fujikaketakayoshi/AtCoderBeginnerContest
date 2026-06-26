import sys
input = sys.stdin.readline
from fractions import Fraction

T = int(input())

for _ in range(T):
  N = int(input())
  A = list(map(int, input().split()))
  # print(N, A)
  B = []
  for a in A:
    B.append((abs(a), a))
  B.sort(reverse=True)
  # print(C)
  ok = True
  r = Fraction(B[0][0], B[1][0])
  for i in range(N - 1):
    if r != Fraction(B[i][0], B[i + 1][0]):
      ok = False
      break
  if ok:
    signs = []
    for b in B:
      if b[1] < 0:
        signs.append('-')
      else:
        signs.append('+')
    # print(not(all(s == '-' for s in signs) or all(s == '+' for s in signs)))
    if not(all(s == '-' for s in signs) or all(s == '+' for s in signs)):
      if signs[0] == '-':
        if not(all(signs[i] == '-' for i in range(0, N, 2))):
          ok = False
        if ok and not(all(signs[i] == '+' for i in range(1, N, 2))):
          ok = False
      else:
        if not(all(signs[i] == '+' for i in range(0, N, 2))):
          ok = False
        if ok and not(all(signs[i] == '-' for i in range(1, N, 2))):
          ok = False
  print('Yes' if ok else 'No')

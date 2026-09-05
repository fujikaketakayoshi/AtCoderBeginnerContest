import sys
input = sys.stdin.readline
from collections import Counter
from fractions import Fraction

N = int(input())
# print(N)

Ns = []
for _ in range(N):
  q = list(map(int, input().split()))
  K, A = q[0], q[1:]
  Ns.append((K, Counter(A)))

ans = 0
for i in range(N):
  for j in range(i + 1, N):
    tmpf = 0
    ki, cnti = Ns[i]
    kj, cntj = Ns[j]
    for v, c in cnti.items():
      fi = Fraction(c, ki)
      if v in cntj:
        fj = Fraction(cntj[v], kj)
        tmpf += fi * fj
    ans = max(ans, tmpf)

print(float(ans))
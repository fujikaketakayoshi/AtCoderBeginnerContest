import sys
input = sys.stdin.readline
import bisect
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, M, A, B)

Ats = []
for i, a in enumerate(A):
  Ats.append((a, i))
Ats.sort()
# print(Ats)

Ais = []
Aidxs = defaultdict(list)

for a, i in Ats:
  Ais.append(a)
  Aidxs[a].append(i)
# print(Ais)
# print(Aidxs)

for idxs in Aidxs.values():
  idxs.sort()
# print(Aidxs)

for b in B:
  l = bisect.bisect_left(Ais, b)
  r = bisect.bisect_right(Ais, b)
  # print(b, l, r)
  if r == 0:
    print(-1)
  elif l == r:
    k = Ais[l - 1]
    print(Aidxs[k][0] + 1)
  elif r - l == 1:
    if l == 0:
      k = Ais[0]
      print(Aidxs[k][0] + 1)
    else:
      k = Ais[l - 1]
      print(Aidxs[k][0] + 1)
  elif l == 0:
    k = Ais[l]
    print(Aidxs[k][0] + 1)
  else:
    k = Ais[l]
    print(Aidxs[k][0] + 1)
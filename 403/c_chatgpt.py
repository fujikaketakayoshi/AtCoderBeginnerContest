import sys
input = sys.stdin.readline
from collections import defaultdict

N, M, Q = map(int, input().split())
# print(N, M, Q)

Xcan = defaultdict(set)
Xall = defaultdict(int)

for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    X, Y = q[1], q[2]
    Xcan[X].add(Y)
  elif q[0] == 2:
    X = q[1]
    Xall[X] = 1
  else:
    X, Y = q[1], q[2]
    if Xall[X]:
      print('Yes')
    elif Y in Xcan[X]:
      print('Yes')
    else:
      print('No')

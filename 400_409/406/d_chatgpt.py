import sys
input = sys.stdin.readline
from collections import defaultdict

H, W, N = map(int, input().split())
# print(H, W, N)

xgars = defaultdict(set)
ygars = defaultdict(set)
for _ in range(N):
  X, Y = map(int, input().split())
  xgars[X].add(Y)
  ygars[Y].add(X)
# print(xgars)
# print(ygars)

Q = int(input())
# print(Q)
for _ in range(Q):
  q, xy = map(int, input().split())
  if q == 1:
    x = xy
    # print(xgars[x].keys())
    print(len(xgars[x]))
    for y in xgars[x]:
      ygars[y].remove(x)
    del xgars[x]
  else:
    y = xy
    print(len(ygars[y]))
    for x in ygars[y]:
      xgars[x].remove(y)
    del ygars[y]

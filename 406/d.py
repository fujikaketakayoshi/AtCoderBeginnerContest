import sys
input = sys.stdin.readline
from collections import defaultdict

H, W, N = map(int, input().split())
# print(H, W, N)

xgars = defaultdict(dict)
ygars = defaultdict(dict)
for _ in range(N):
  X, Y = map(int, input().split())
  xgars[X][Y] = 1
  ygars[Y][X] = 1
# print(xgars)
# print(ygars)

Q = int(input())
# print(Q)
for _ in range(Q):
  q, xy = map(int, input().split())
  if q == 1:
    x = xy
    # print(xgars[x].keys())
    keys = list(xgars[x].keys())
    remove_x = len(keys)
    del xgars[x]
    for k in keys:
      del ygars[k][x]
    print(remove_x)
  else:
    y = xy
    keys = list(ygars[y].keys())
    remove_y = len(keys)
    del ygars[y]
    for k in keys:
      del xgars[k][y]
    print(remove_y)

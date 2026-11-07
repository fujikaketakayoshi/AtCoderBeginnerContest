import sys
input = sys.stdin.readline
from collections import defaultdict
from sortedcontainers import SortedSet

import bisect

N, M, Sx, Sy = map(int, input().split())
# print(N, M, Sx, Sy)

Hx = defaultdict(SortedSet)
Hy = defaultdict(SortedSet)
for _ in range(N):
  X, Y = map(int, input().split())
  # print(X, Y)
  Hx[X].add(Y)
  Hy[Y].add(X)
# print(Hx, Hy)

ans = set()
for _ in range(M):
  # print(Sx, Sy)
  D, C = input().split()
  C = int(C)
  if D == 'U':
    Ny = Sy + C
    l = bisect.bisect_left(Hx[Sx], Sy)
    r = bisect.bisect_right(Hx[Sx], Ny)
    # print(l, r, xs[l], xs[r])
    targets = Hx[Sx][l:r]
    for t in targets:
      ans.add((Sx, t))
      Hx[Sx].discard(t)
      Hy[t].discard(Sx)
    Sy = Ny
  elif D == 'D':
    Ny = Sy - C
    l = bisect.bisect_left(Hx[Sx], Ny)
    r = bisect.bisect_right(Hx[Sx], Sy)
    # print(l, r, xs[l], xs[r])
    targets = Hx[Sx][l:r]
    for t in targets:
      ans.add((Sx, t))
      Hx[Sx].discard(t)
      Hy[t].discard(Sx)
    Sy = Ny
  elif D == 'L':
    Nx = Sx - C
    l = bisect.bisect_left(Hy[Sy], Nx)
    r = bisect.bisect_right(Hy[Sy], Sx)
    # print(Hy[Sy][l], l, r)
    targets = Hy[Sy][l:r]
    for t in targets:
      ans.add((t, Sy))
      Hy[Sy].discard(t)
      Hx[t].discard(Sy)
    Sx = Nx
  else:
    Nx = Sx + C
    l = bisect.bisect_left(Hy[Sy], Sx)
    r = bisect.bisect_right(Hy[Sy], Nx)
    # print(l, r, xs[l], xs[r])
    targets = Hy[Sy][l:r]
    for t in targets:
      ans.add((t, Sy))
      Hy[Sy].discard(t)
      Hx[t].discard(Sy)
    Sx = Nx
  # print(Nx, Ny)
print(Sx, Sy, len(ans))
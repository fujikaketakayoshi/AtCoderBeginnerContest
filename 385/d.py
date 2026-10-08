import sys
input = sys.stdin.readline
from collections import defaultdict
import bisect

N, M, Sx, Sy = map(int, input().split())
# print(N, M, Sx, Sy)

Hx = defaultdict(list)
Hy = defaultdict(list)
for _ in range(N):
  X, Y = map(int, input().split())
  # print(X, Y)
  Hx[X].append(Y)
  Hy[Y].append(X)

for k in Hx.keys():
  Hx[k].sort()

for k in Hy.keys():
  Hy[k].sort()

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
    for i in range(l, r):
      ans.add((Sx, Hx[Sx][i]))
      # Hx[Sx].discard(ys[i])
      # Hy[ys[i]].discard(Sx)
    if r == l:
      1
    elif r - 1 == l:
      Hx[Sx].pop(l)
    else:
      Hx[Sx] = Hx[Sx][0:l] + Hx[Sx][r:]
    Sy = Ny
  elif D == 'D':
    Ny = Sy - C
    l = bisect.bisect_left(Hx[Sx], Ny)
    r = bisect.bisect_right(Hx[Sx], Sy)
    # print(l, r, xs[l], xs[r])
    for i in range(l, r):
      ans.add((Sx, Hx[Sx][i]))
      # Hx[Sx].discard(ys[i])
      # Hy[ys[i]].discard(Sx)
    if r == l:
      1
    elif r - 1 == l:
      Hx[Sx].pop(l)
    else:
      Hx[Sx] = Hx[Sx][0:l] + Hx[Sx][r:]
    Sy = Ny
  elif D == 'L':
    Nx = Sx - C
    l = bisect.bisect_left(Hy[Sy], Nx)
    r = bisect.bisect_right(Hy[Sy], Sx)
    # print(Hy[Sy], l, r)
    for i in range(l, r):
      ans.add((Hy[Sy][i], Sy))
      # Hy[Sy].discard(xs[i])
      # Hx[xs[i]].discard(Sy)
    if r == l:
      1
    elif r - 1 == l:
      Hy[Sy].pop(l)
    else:
      Hy[Sy] = Hy[Sy][0:l] + Hy[Sy][r:]
    # print(Hy[Sy])
    Sx = Nx
  else:
    Nx = Sx + C
    l = bisect.bisect_left(Hy[Sy], Sx)
    r = bisect.bisect_right(Hy[Sy], Nx)
    # print(l, r, xs[l], xs[r])
    for i in range(l, r):
      ans.add((Hy[Sy][i], Sy))
    if r == l:
      1
    elif r - 1 == l:
      Hy[Sy].pop(l)
    else:
      Hy[Sy] = Hy[Sy][0:l] + Hy[Sy][r:]
    Sx = Nx
  # print(Nx, Ny)
print(Sx, Sy, len(ans))
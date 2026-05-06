import sys
input = sys.stdin.readline
from collections import deque


Rt, Ct, Ra, Ca = map(int, input().split())
# print(Rt, Ct, Ra, Ca)

if (abs(Rt - Ra) + abs(Ct - Ca)) % 2 == 1:
  print(0)
  exit()

N, M, L = map(int, input().split())
# print(N, M, L)
DIR = {
  'R': (0, 1),
  'L': (0, -1),
  'U': (-1, 0),
  'D': (1, 0),
}

Sq = deque()
for _ in range(M):
  d, repeat = map(str, input().split())
  Sq.append((d, int(repeat)))

Tq = deque()
for _ in range(L):
  d, repeat = map(str, input().split())
  Tq.append((d, int(repeat)))

# print(Sq, Tq)
ty, tx = Rt, Ct
ay, ax = Ra, Ca
cnt = 0
tmpSd = ''
tmpSr = 0
tmpTd = ''
tmpTr = 0
while Sq or Tq:
  if tmpSr == 0:
    tmpSd, tmpSr = Sq.popleft()
  if tmpTr == 0:
    tmpTd, tmpTr = Tq.popleft()
  # print(tmpSd, tmpSr, tmpTd, tmpTr)
  n = min(tmpSr, tmpTr)
  tmpSr -= n
  tmpTr -= n
  dSy = DIR[tmpSd][0] * n
  dSx = DIR[tmpSd][1] * n
  dTy = DIR[tmpTd][0] * n
  dTx = DIR[tmpTd][1] * n
  # print(dSy, dSx)
  # print(dTy, dTx)
  nty = ty + dSy
  ntx = tx + dSx
  nay = ay + dTy
  nax = ax + dTx
  if n > 1 and ty == ay and tx == ax and nty == nay and ntx == nax:
    cnt += n
  elif dSy == dTy == 0 and max(tx, ntx) <= min(ax, nax):
    cnt += 1
  elif dSx == dTx == 0 and max(ty, nty) <= min(ay, nay):
    cnt += 1
  elif nty == nay and ntx == nax:
    cnt += 1
  ty = nty
  tx = ntx
  ay = nay
  ax = nax
print(cnt)
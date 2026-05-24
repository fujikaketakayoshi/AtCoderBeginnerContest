import sys
input = sys.stdin.readline
from collections import defaultdict

S = input().strip()
T = input().strip()
lS = len(S)
lT = len(T)

cnt = 0
i = 0
pre = 1
si = 0
ti = 0
while i < lS:
  while si < lS:
    if S[si] == T[ti] and ti == lT - 1:
      # print(lS - si, pre)
      cnt += (lS - si) * pre
      # print(cnt)
      break
    elif S[si] == T[ti] and ti == 0:
      pre = si - i + 1
      ti += 1
      i = si
    elif S[si] == T[ti]:
      ti += 1
    si += 1
  ti = 0
  i += 1
  si = i

print((1 + lS) * lS // 2 - cnt)

import sys
input = sys.stdin.readline
from collections import deque

Q = int(input())

dq = deque()
preT = [0]
totalT = 0
tidx = 0
for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    dq.append(tidx)
  elif q[0] == 2:
    T = q[1]
    totalT += T
    preT.append(totalT)
    tidx += 1
  else:
    H = q[1]
    cnt = 0
    while dq and preT[tidx] - preT[dq[0]] >= H:
      dq.popleft()
      cnt += 1
    print(cnt)

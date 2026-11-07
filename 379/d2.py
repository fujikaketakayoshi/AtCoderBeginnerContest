import sys
input = sys.stdin.readline
from collections import deque

Q = int(input())

dq = deque()
totalT = 0
for _ in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    dq.append(totalT)
  elif q[0] == 2:
    T = q[1]
    totalT += T
  else:
    H = q[1]
    cnt = 0
    while dq and totalT - dq[0] >= H:
      dq.popleft()
      cnt += 1
    print(cnt)

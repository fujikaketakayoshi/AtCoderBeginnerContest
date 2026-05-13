import sys
input = sys.stdin.readline
import math

T = int(input())

for _ in range(T):
  cnt = 0
  C, D = map(int, input().split())
  lC = len(str(C))
  start = int(str(C) + str(C + 1))
  end = int(str(C) + str(C + D))
  sstart = math.ceil(start ** 0.5)
  send = math.floor(end ** 0.5)
  # print(start, end)
  # print(start ** 0.5, end ** 0.5)
  for i in range(sstart, send + 1):
    hi = i ** 2
    if str(C) == str(hi)[0:lC]:
      # print(str(C), str(i ** 2), str(i ** 2)[0:lC])
      simo = str(hi)[lC:]
      # print(str(i ** 2)[lC:])
      if simo[0] != '0' and 1 <= int(simo) - C <= D:
        cnt += 1
  print(cnt)
  
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
used = set()

cnt = 0
for m in range(M):
  R, C = map(int, input().split())
  ok = True
  for dr in (-1, 0, 1):
    for dc in (-1, 0, 1):
        if (R + dr, C + dc) in used:
            ok = False
            break
  if ok:
    used.add((R, C))
    cnt += 1

print(cnt)

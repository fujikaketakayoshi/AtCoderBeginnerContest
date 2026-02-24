import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
grid = defaultdict(int)


cnt = 0
for m in range(M):
  R, C = map(int, input().split())
  if grid[(R - 1, C - 1)] == 0 and grid[(R, C - 1)] == 0 and grid[(R - 1, C)] == 0 and grid[(R, C)] == 0:
    grid[(R - 1, C - 1)] = 1
    grid[(R, C - 1)] = 1
    grid[(R - 1, C)] = 1
    grid[(R, C)] = 1
    cnt += 1

print(cnt)

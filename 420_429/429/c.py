import sys
input = sys.stdin.readline
from collections import defaultdict
import math

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1
if len(cnt.keys()) == N or len(cnt.keys()) == 1:
  print(0)
  exit()

# print(cnt)
times = 0
for v in cnt.values():
  if v == 1:
    continue
  times += math.comb(v, 2) * (N - v)
  # print(v, times)
print(times)

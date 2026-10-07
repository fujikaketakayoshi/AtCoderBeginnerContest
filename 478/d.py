import sys
input = sys.stdin.readline
from collections import defaultdict

N, Q = map(int, input().split())
# print(N, Q)

cnt = defaultdict(list)
for _ in range(Q):
  L, R, X = map(int, input().split())
  cnt[X].append((L, R))

# print(cnt)

imos = [0] * (N + 2)

for lrs in cnt.values():
  lmin = 10 ** 30
  rmax = 0
  lrs.sort()
  for l, r in lrs:
    if rmax <= l:
      start = l
      end = r
      rmax = r
      lmin = min(lmin, l)
    elif l < rmax:
      start = rmax + 1
      if r < rmax:
        start = None
        end = None
      else:
        end = r
        rmax = r
    if start and end:
      imos[start] += 1
      imos[end + 1] -= 1
  # print(imos)
# print(imos)

ans = []
av = 0
for v in imos:
  av += v
  ans.append(av)

print(*ans[1:-1])
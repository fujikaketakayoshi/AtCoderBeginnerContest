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
  rmax = 0
  lrs.sort()
  for l, r in lrs:
    if r <= rmax:
      continue
    elif rmax < l:
      start = l
      end = r
      rmax = r
    else:
      start = rmax + 1
      end = r
      rmax = r
    imos[start] += 1
    imos[end + 1] -= 1
  # print(imos)
# print(imos)

ans = []
tmp = 0
for v in imos:
  tmp += v
  ans.append(tmp)

print(*ans[1:-1])
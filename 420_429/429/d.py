import sys
input = sys.stdin.readline
from collections import defaultdict

N, M, C = map(int, input().split())
A = list(map(int, input().split()))
# print(N, M, C, A)
A.sort()

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1
# print(cnt)

xcnt = defaultdict(int)
for k, v in cnt.items():
  tmp_cnt = v
  j = 1
  while tmp_cnt < C:
    tmp_cnt += cnt.get((k + j) % M, 0)
    j += 1
  xcnt[k] = tmp_cnt
# print(xcnt)

ikeys = list(xcnt.keys())
# print(ikeys)
ans = 0
for idx, i in enumerate(ikeys):
  if idx == 0 and i != 0:
    ans += i * xcnt[i]
  if idx == len(ikeys) - 1:
    ans += (M - i) * xcnt[i]
  else:
    ans += (ikeys[idx + 1] - i) * xcnt[i]

print(ans)

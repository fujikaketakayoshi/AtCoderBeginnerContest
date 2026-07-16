import sys
input = sys.stdin.readline
from collections import defaultdict

N, D = map(int, input().split())
# print(N, D)
A = list(map(int, input().split()))
A.sort()
# print(A)

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1
# print(cnt)

ans = 0
keys = set(cnt.keys())
# print(keys)
tmp_keys = keys.copy()
for k in tmp_keys:
  up = k + D
  pre = k
  tmp = []
  while up in keys:
    keys.remove(pre)
    tmp.append([pre, cnt[pre]])
    up = pre + D
    pre = up
  # print(tmp)
  for i in range(len(tmp) - 1):
    delnum = min(tmp[i][1], tmp[i + 1][1])
    tmp[i][1] -= delnum
    tmp[i + 1][1] -= delnum
    ans += delnum
print(ans)
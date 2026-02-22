import sys
input = sys.stdin.readline
from collections import defaultdict
import bisect


N = int(input().strip())
A = list(map(int, input().split()))

cnt = defaultdict(list)
for i, a in enumerate(A):
  cnt[a].append(i)

Aset = sorted(set(A))
# print(cnt)
max_ans = 0
for a in Aset:
  # print(a)
  for i in cnt[a]:
    ans = 1
    idx = i
    v = a
    while v + 1 in cnt:
      next_idx = bisect.bisect_left(cnt[v + 1], idx)
      # print(ans, v, idx, v + 1, next_idx)
      if next_idx < len(cnt[v + 1]) and cnt[v + 1][next_idx] > idx:
        idx = cnt[v + 1][next_idx]
        ans += 1
        v += 1
      else:
        break
    max_ans = max(max_ans, ans)
print(max_ans)

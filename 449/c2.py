import sys
input = sys.stdin.readline
from collections import defaultdict
import bisect

N, L, R = map(int, input().split())
S = input().strip()
# print(N, L, R)
# print(S)
cnt = defaultdict(list)
for i, c in enumerate(S):
  cnt[c].append(i)

ans = 0
for k, idxs in cnt.items():
  # print(k, idxs)
  for i in range(len(idxs)):
    l = bisect.bisect_left(idxs, idxs[i] + L)
    r = bisect.bisect_right(idxs, idxs[i] + R)
    # print(l, r)
    ans += r - l
print(ans)

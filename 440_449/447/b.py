import sys
input = sys.stdin.readline
from collections import defaultdict

S = input().strip()

cnt = defaultdict(int)
for c in S:
  cnt[c] += 1

cnt_desc = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
max_cnt = cnt_desc[0][1]

ex_c = set()
for c, v in cnt_desc:
  if max_cnt == v:
    ex_c.add(c)
  else:
    break

ans = ''
for c in S:
  if not c in ex_c:
    ans += c

print(ans)
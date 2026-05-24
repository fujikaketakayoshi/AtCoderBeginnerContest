import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

N = int(input())

for _ in range(N):
  cnt = defaultdict(int)
  S = input().strip()
  for c in S:
    cnt[c] += 1
  words = list(cnt.keys())
  cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
  max_cnt = cnt[0][1]
  max_c = cnt[0][0]
  rem_cnt = 0
  for k, v in cnt[1:]:
    rem_cnt += v
  if max_cnt - rem_cnt <= 1:
    print('Yes')
    
    hq = []  # 空のヒープを作る
    for k, v in cnt[1:]:
      heapq.heappush(hq, [-v, k])
    # print(hq)
    results = [max_c]
    pre = [ -1 * (max_cnt - 1), max_c]
    while len(results) < len(S):
      v, k = heapq.heappop(hq)
      results.append(k)
      heapq.heappush(hq, pre)
      nv = -v - 1
      pre = [-nv, k]
    print(''.join(results))
  else:
    print('No')
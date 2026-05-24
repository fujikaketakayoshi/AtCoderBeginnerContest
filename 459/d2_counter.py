import sys
input = sys.stdin.readline
from collections import Counter
import heapq

N = int(input())

for _ in range(N):
  S = input().strip()
  cnt = Counter(S)
  words = list(cnt.keys())
  # most = cnt.most_common(1)
  # cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
  max_cnt = cnt.most_common(1)[0][1]
  # max_c = most[0][0]
  all_cnt = 0
  for v in cnt.values():
    all_cnt += v
  if max_cnt - (all_cnt - max_cnt) <= 1:
    print('Yes')
    
    hq = []  # 空のヒープを作る
    for k, v in cnt.items():
      heapq.heappush(hq, [-v, k])
    # print(hq)
    max_v, max_k = heapq.heappop(hq)
    results = [max_k]
    pre = [max_v + 1, max_k]
    while len(results) < len(S):
      v, k = heapq.heappop(hq)
      results.append(k)
      heapq.heappush(hq, pre)
      pre = [v + 1, k]
    print(''.join(results))
  else:
    print('No')
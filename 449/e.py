import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
# print(N, M, A)

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1

flat_cnt = 0
max_cnt = max(cnt.values())
q = []
for i in range(1, M + 1):
  flat_cnt += max_cnt - cnt[i]
  heapq.heappush(q, (cnt[i], i))
flat_len = N + flat_cnt

for f in range(flat_len):
  num_cnt, num = heapq.heappop(q)
  heapq.heappush(q, (num_cnt + 1, num))
  A.append(num)

Q = int(input())
# print(Q)
for _ in range(Q):
  q = int(input())
  if q > flat_len:
    amari = (q - flat_len) % M
    print(amari if amari != 0 else M)
  else:
    print(A[q - 1])

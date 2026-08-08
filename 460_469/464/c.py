import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())

cnt = defaultdict(int)
changes = [[] for _ in range(M + 1)]
for i in range(1, N + 1):
  A, D, B = map(int, input().split())
  changes[D].append((A, B))
  cnt[A] += 1
# print(changes)

ans = len(cnt.keys())
for d in range(1, M + 1):
  for a, b in changes[d]:
    if a == b:
      continue
    if cnt[a] == 1:
      ans -= 1
    if cnt[b] == 0:
      ans += 1
    cnt[a] -= 1
    cnt[b] += 1
    
  print(ans)
import sys
input = sys.stdin.readline
from collections import defaultdict

N, L = map(int, input().split())
D = [0] + list(map(int, input().split()))
# print(N, L, D)

if L % 3 > 0:
  print(0)
  exit()

cnt = defaultdict(int)
dist = 0
for d in D:
  dist += d
  cnt[dist % L] += 1
# print(cnt)

ans = 0
kankaku = L // 3
for i in range(kankaku):
  # print(i, i + kankaku, i + 2 * kankaku)
  ans += cnt[i] * cnt[i + kankaku] * cnt[i + 2 * kankaku]

print(ans)

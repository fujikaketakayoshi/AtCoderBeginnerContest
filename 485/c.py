import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))
# print(N, C)

cnt = defaultdict(list)
suc = 0
lc = C[0]
li = 0
for i in range(1, N):
  if C[i] == lc:
    suc += 1
  elif C[i] != lc and suc == 0:
    cnt[lc].append((li, li))
    lc = C[i]
    li = i
  elif C[i] != lc and suc > 0:
    cnt[lc].append((li, i - 1))
    lc = C[i]
    li = i
i += 1
if suc == 0:
  cnt[lc].append((li, li))
else:
  cnt[lc].append((li, i - 1))
# print(cnt)

cntidx = defaultdict(lambda: defaultdict(int))
for k, v in cnt.items():
  for i, t in enumerate(v):
    l = t[0]
    r = t[1]
    for idx in range(l, r + 1):
      cntidx[k][idx] = i
# print(cntidx)

ans = []
for n in range(N):
  c = C[n]
  tidx = cntidx[c][n]
  l = cnt[c][tidx][0]
  r = cnt[c][tidx][1]
  if l == r:
    ans.append(1)
    continue
    # print(1)
  if l == 0:
    l = float('-INF')
  if r == N - 1:
    r = float('INF')
  ans.append(min(n - (l - 1), (r + 1) - n))
  # print(cnt[c][tidx])

print(*ans)
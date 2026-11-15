import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

cnt = defaultdict(list)
pre = A[0]
suc = 1
for a in A[1:]:
  if pre == a:
    suc += 1
  else:
    cnt[a].append(suc)
    pre = a
    suc = 1
cnt[pre].append(suc)
# print(cnt)

ans = N * (N - 1) // 2
# print(ans)

for k, vs in cnt.items():
  for i, suc in enumerate(vs):
    if i == 0 and suc == 1:
      continue
    ans -= suc
print(ans)
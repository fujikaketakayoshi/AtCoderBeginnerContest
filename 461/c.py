import sys
input = sys.stdin.readline
from collections import defaultdict

N, K, M = map(int, input().split())
# print(N, K, M)

VC = []
Cmax = defaultdict(int)
Cidx = defaultdict(int)
for n in range(N):
  C, V = map(int, input().split())
  if Cmax[C] < V:
    Cmax[C] = V
    Cidx[C] = n
  VC.append((V, C, n))
VC.sort(reverse=True)

sorted_Cmax = sorted(Cmax.items(), key=lambda x: x[1], reverse=True)
# print(sorted_Cmax)

used_idx = set()
ans = 0
cnt = 0
for i in range(M):
  C = sorted_Cmax[i][0]
  V = sorted_Cmax[i][1]
  used_idx.add(Cidx[C])
  ans += V
  cnt += 1

for V, C, n in VC:
  if K <= cnt:
    break
  if n in used_idx:
    continue
  ans += V
  cnt += 1

print(ans)
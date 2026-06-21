import sys
input = sys.stdin.readline
import bisect

N, K = map(int, input().split())
# print(N, K)

LR = []
for _ in range(N):
  L, R = map(int, input().split())
  LR.append((L, R))
LR.sort()
print(LR)

L = []
for l, r in LR:
  L.append(l)
print(L)

result = []
i = 0
while i < N:
  cnt = 0
  min_dis = float('INF')
  idx = bisect.bisect_right(L, LR[i][1])
  while idx < N:
    min_dis = min(min_dis, LR[idx][0] - LR[i][1])
    cnt += 1
    idx = bisect.bisect_right(L, LR[idx][1])
  print(i, cnt)
  if cnt + 1 >= K:
    result.append(min_dis)
  i += 1

print(max(result) if result else -1)
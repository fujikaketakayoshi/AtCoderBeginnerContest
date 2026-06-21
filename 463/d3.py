import sys
input = sys.stdin.readline
import bisect

N, K = map(int, input().split())
# print(N, K)

LR = []
for _ in range(N):
  L, R = map(int, input().split())
  LR.append((L, R))
LR.sort(key=lambda x: x[1])
print(LR)

L = []
for l, r in LR:
  L.append(l)
print(L)

result = []
cnt = 1
last_r = float('-INF')
min_dis = float('INF')
for l, r in LR:
  if l > last_r:
    cnt += 1
    min_dis = min(min_dis, l - last_r)
  last_r = r

print(cnt)
print(min_dis if cnt >= K else -1)
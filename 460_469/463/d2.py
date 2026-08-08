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

i = 1
cnt = 1
min_dis = float('INF')
prel = LR[0][0]
prer = LR[0][1]
prew = prer - prel
while i < N:
  l = LR[i][0]
  r = LR[i][1]
  if r < prer:
    prel = l
    prer = r
    i += 1
    continue
  if prer < l:
    min_dis = min(min_dis, l - prer)
    cnt += 1
    i += 1
    continue
  i += 1

print(cnt, min_dis)
  
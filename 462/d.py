import sys
input = sys.stdin.readline
import math

N, D = map(int, input().split())
# print(N, D)
MAX = 10 ** 6 + 1
# MAX = 30

presum = [0] * MAX 
for _ in range(N):
  S, T = map(int, input().split())
  presum[S] += 1
  presum[T] -= 1
  # print(S, T)

# print(presum)
kukan = [0] * (MAX + 1)
for i in range(1, MAX):
  kukan[i] = kukan[i - 1] + presum[i]

i = 0
ans = 0
while i + D < MAX + 1:
  kukan_min = float('INF')
  ok = True
  for j in range(i, i + D):
    if kukan[j] >= 2:
      kukan_min = min(kukan_min, kukan[j])
    else:
      ok = False
      break
  if ok:
    ans += math.comb(kukan_min, 2)
  i += 1
print(ans)
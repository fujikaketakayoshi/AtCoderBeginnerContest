import sys
input = sys.stdin.readline
import math

N, M = map(int, input().split())
# print(N, M)

AB = set()
cnt = [0] * N
for m in range(M):
  A, B = map(int, input().split())
  AB.add((A, B))
  mod = (A + B) % N
  cnt[mod] += 1
# print(cnt)

heikou = 0
for v in cnt:
  heikou += math.comb(v, 2)
print(math.comb(M, 2) - heikou)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

wall = [0] * (N + 1)

for _ in range(M):
  L, R = map(int, input().split())
  L -= 1
  R -= 1
  wall[L] += 1
  wall[R + 1] -= 1
# print(wall)

presum = [0] * (N + 1)
presum[0] = wall[0]
for i in range(1, N + 1):
  presum[i] = presum[i - 1] + wall[i]
# print(presum)

print(min(presum[:-1]))

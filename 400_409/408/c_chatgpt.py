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

cur = 0
ans = M
for i in range(N):
    cur += wall[i]
    ans = min(ans, cur)
print(ans)

import sys
input = sys.stdin.readline

SKY = 2000
N = int(input())
# print(N)

grid = [[0] * (SKY + 1) for _ in range(SKY + 1)]
clouds = []
total = 0
for i in range(N):
  U, D, L, R = map(int, input().split())
  clouds.append((U, D, L, R))
  # print(U, D, L, R)
  for r in range(U, D + 1):
    for c in range(L, R + 1):
      if grid[r][c] == 0:
        total += 1
      grid[r][c] += 1

for i in range(N):
  clear_cnt = 0
  U, D, L, R = clouds[i]
  for r in range(U, D + 1):
    for c in range(L, R + 1):
      if grid[r][c] == 1:
        clear_cnt += 1
  print(SKY * SKY - (total - clear_cnt))


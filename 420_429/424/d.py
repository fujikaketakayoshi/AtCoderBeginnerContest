import sys
input = sys.stdin.readline

T = int(input())
# print(T)

for _ in range(T):
  H, W = map(int, input().split())
  # print(H, W)
  grid = []
  for h in range(H):
    grid.append(list(input().strip()))
  # counted = [[False] * W for _ in range(H)]
  black_num = [[0] * W for _ in range(H)]
  # print(grid)
  # print(counted)
  # print(black_num)
  
  ans = 0
  for h in range(H - 1):
    for w in range(W - 1):
      for y in range(h, h + 2):
        for x in range(w, w + 2):
          if grid[y][x] == '#':
            black_num[h][w] += 1
      if black_num[h][w] == 4:
        grid[h + 1][w + 1] = '.'
        ans += 1
  # print(black_num)
  print(ans)

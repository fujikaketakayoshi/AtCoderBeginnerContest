import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = []
q = []
ans = 0
for h in range(H):
  raw = list(input().strip())
  for i, r in enumerate(raw):
    if r == '#':
      q.append((h, i))
      ans += 1
  grid.append(raw)

if len(q) == 0:
  print(0)
  exit()

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

i = 0
while q:
  next_blacks = []
  for y, x in q:
    # print(i, y, x)
  
    for d in range(4):
      ny = y + DIR[d][0]
      nx = x + DIR[d][1]
      if not (0 <= ny < H and 0 <= nx < W):
        continue
      if grid[ny][nx] == '.':
        b_cnt = 0
        for d in range(4):
          n2y = ny + DIR[d][0]
          n2x = nx + DIR[d][1]
          if not (0 <= n2y < H and 0 <= n2x < W):
            continue
          if grid[n2y][n2x] == '#':
            b_cnt += 1
        if b_cnt == 1:
          next_blacks.append((ny, nx))
          ans += 1
  q = []
  for ty, tx in next_blacks:
    grid[ty][tx] = '#'
    q.append((ty, tx))
  i += 1
print(ans)

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
maxHW = max(H, W)

grid = []
for _ in range(H):
  grid.append(list(input().strip()))

part = []
grid2 = [['.'] * W for _ in range(H)]
part.append(grid)
part.append(grid2)

DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

cnt = 0
while cnt < maxHW:
  if cnt % 2 == 0:
    now = 0
    next = 1
  else:
    now = 1
    next = 0
  
  for h in range(H):
    for w in range(W):
      if part[now][h][w] == '.':
        ok = False
        for dy, dx in DIR:
          ny = h + dy
          nx = w + dx
          if not(0 <= ny < H and 0 <= nx < W):
            continue
          if part[now][ny][nx] == '#':
            part[next][h][w] = '#'
            ok = True
            break
        if not ok:
          part[next][h][w] = '.'
      else:
        part[next][h][w] = '.'
  cnt += 1

for row in part[0]:
  print(''.join(row))

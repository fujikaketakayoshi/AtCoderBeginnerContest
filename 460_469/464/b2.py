import sys
input = sys.stdin.readline

H, W = map(int, input().split())

grid = []
for _ in range(H):
  S = list(input().strip())
  grid.append(S)

for h in range(H):
  if any(r == '#' for r in grid[h]):
    lh = h
    break

for h in range(H - 1, -1, -1):
  if any(r == '#' for r in grid[h]):
    rh = h
    break

# print(lh, rh)

for w in range(W):
  ok = False
  for h in range(H):
    if grid[h][w] == '#':
      lw = w
      ok = True
      break
  if ok:
    break

for w in range(W - 1, -1, -1):
  ok = False
  for h in range(H):
    if grid[h][w] == '#':
      rw = w
      ok = True
      break
  if ok:
    break

# print(lw, rw)

for h in range(lh, rh + 1):
  print(''.join(grid[h][lw:rw + 1]))
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
# print(H, W)
MAX = 1001
grid = []
l = MAX
r = -1
t = MAX
b = -1
for h in range(H):
  S = input().strip()
  grid.append(S)
  for w, c in enumerate(S):
    if c == '#':
      l = min(l, w)
      r = max(r, w)
      t = min(t, h)
      b = max(b, h)
# print(grid)
# print(l,r,t,b)

for i in range(t, b + 1):
  for j in range(l, r + 1):
    if grid[i][j] == '.':
      print('No')
      exit()

print('Yes')

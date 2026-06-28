import sys
input = sys.stdin.readline

H, W = map(int, input().split())

grid = []
for _ in range(H):
  row = list(input().strip())
  grid.append(row)

n1 = []
ok = False
for h in range(H):
  if any(r == '#' for r in grid[h]):
    ok = True
  if ok:
    n1.append(grid[h])
# print(n1)

n2 = []
ok = False
for h in range(len(n1) - 1, -1, -1):
  if any(r == '#' for r in n1[h]):
    ok = True
  if ok:
    n2.append(n1[h])
n2.reverse()
# print(n2)

n3 = []
ok = False
for w in range(len(n2[0])):
  row = []
  for h in range(len(n2)):
    row.append(n2[h][w])
  n3.append(row)
# print(n3)

n4 = []
ok = False
for w in range(W):
  if any(r == '#' for r in n3[w]):
    ok = True
  if ok:
    n4.append(n3[w])
# print(n4)

n5 = []
ok = False
for w in range(len(n4) - 1, -1, -1):
  if any(r == '#' for r in n4[w]):
    ok = True
  if ok:
    n5.append(n4[w])
n5.reverse()
# print(n5)

ans = []
for h in range(len(n5[0])):
  row = []
  for w in range(len(n5)):
    row.append(n5[w][h])
  ans.append(row)
# print(ans)

for a in ans:
  print(''.join(a))
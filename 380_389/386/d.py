import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
# print(N, M)

row = defaultdict(list)
col = defaultdict(list)

for _ in range(M):
  X, Y, C = input().split()
  X, Y = int(X), int(Y)
  # print(X, Y, C)
  row[X].append((Y, C))
  col[Y].append((X, C))

# print(row)
# print(col)

preBmax = N + 1
# preWmin = 0
for r in sorted(row.keys()):
  Brmax = 0
  Wrmin = N + 1
  for c, C in row[r]:
    # print(r, c, C, Brmax, Wrmin)
    if C == 'B':
      Brmax = max(Brmax, c)
    elif C == 'W':
      Wrmin = min(Wrmin, c)
    # print('!', Brmax, Wrmin, Brmax > Wrmin)
    if Brmax != 0 and Wrmin != N + 1 and Brmax > Wrmin:
      print('No')
      exit()
    # print('!!', Brmax, preBmax, Brmax > preBmax)
    # if Brmax > preBmax or Wrmin < preWmin:
    if Brmax > preBmax:
      print('No')
      exit()
  if Wrmin != N + 1:
    preBmax = Wrmin - 1
    # preWmin = Wrmin

preBmax = N + 1
# preWmin = 0
for c in sorted(col.keys()):
  Bcmax = 0
  Wcmin = N + 1
  for r, C in col[c]:
    # print(c, r, C, Bcmax, Wcmin)
    if C == 'B':
      Bcmax = max(Bcmax, r)
    elif C == 'W':
      Wcmin = min(Wcmin, r)
    # print('!', Bcmax, Wcmin, preBmax, Bcmax > Wcmin)
    if Bcmax != 0 and Wcmin != N + 1 and Bcmax > Wcmin:
      print('No')
      exit()
    if Bcmax > preBmax :
      print('No')
      exit()
  if Wcmin != N + 1:
    preBmax = Wcmin - 1
    # preWmin = Wcmin

print('Yes')

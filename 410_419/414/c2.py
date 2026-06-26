import sys
input = sys.stdin.readline
# from itertools import product
sys.setrecursionlimit(10**7)

A = int(input())
N = int(input())
# print(A, N)

def base_n(num, base):
    if num == 0:
        return "0"

    s = ""
    while num:
        s = str(num % base) + s
        num //= base

    return s

AN = base_n(N, A)

slist0 = list(map(str, range(A)))
slist = list(map(str, range(1, A)))

palA = []

def dfs(path):
  # if path != '':
  #   print(path, int(path, A))
  if path != '' and len(path) > len(AN):
    return
  if len(path) == 0:
    for i in slist0:
      palA.append(i)
      dfs(i)
      palA.append(i + i)
      dfs(i + i)
  else:
    for i in slist:
      palA.append(i + path + i)
      dfs(i + path + i)
dfs('')

candA = []
for p in palA:
  ip = int(p, A)
  if p[0] != '0' and ip <= N:
    candA.append(p)
# print(candA)

ans = 0
for c in candA:
  iN = int(c, A)
  sN = str(iN)
  if sN == sN[::-1]:
    ans += iN
print(ans)
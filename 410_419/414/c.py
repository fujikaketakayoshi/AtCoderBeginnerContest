import sys
input = sys.stdin.readline
# from itertools import product

A = int(input())
N = int(input())
# print(A, N)

ten = list(map(str, range(10)))

palN = []

def dfs(path):
  if len(path) > len(str(N)):
    return
  for i in ten:
    if len(path) == 0:
      palN.append(i)
      dfs(i)
      palN.append(i + i)
      dfs(i + i)
    else:
      palN.append(i + path + i)
      dfs(i + path + i)
dfs('')
# print(palN)

def base_n(num, base):
    if num == 0:
        return "0"

    s = ""
    while num:
        s = str(num % base) + s
        num //= base

    return s

candN = []
for p in palN:
  ip = int(p)
  if p[0] != '0' and ip <= N:
    candN.append(ip)
# print(candN)

ans = 0
for c in candN:
  s = base_n(c, A)
  if s == s[::-1]:
    ans += c
print(ans)
import sys
input = sys.stdin.readline
# from itertools import product

A = int(input())
N = int(input())
# print(A, N)

ten = list(map(str, range(10)))

def base_n(num, base):
    if num == 0:
        return "0"

    s = ""
    while num:
        s = str(num % base) + s
        num //= base

    return s

ans = 0

def dfs(path):
  global ans
  ip = int(path) if path != '' else 0
  if ip > N or len(path) > len(str(N)):
    return
  
  if path != '' and path[0] != '0':
    a = base_n(ip, A)
    if a == a[::-1]:
      ans += ip
  
  for i in ten:
    if len(path) == 0:
      dfs(i)
      dfs(i + i)
    else:
      dfs(i + path + i)
dfs('')

print(ans)

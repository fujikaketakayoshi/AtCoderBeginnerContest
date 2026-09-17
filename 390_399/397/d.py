import sys
input = sys.stdin.readline

N = int(input())
# print(N)

MAX = 10 ** 6 * 2

l = 1
r = MAX
while l + 1 < r:
  xlarge = False
  x = (l + r) // 2
  jl = 1
  jr = x
  while jl + 1 < jr:
    y = (jl + jr) // 2
    # print(jl, jr, x, y, x ** 3 - y ** 3)
    if x ** 3 - y ** 3 == N:
      print(x, y)
      exit()
    elif x ** 3 - y ** 3 > N:
      jl = y
    else:
      xlarge = True
      l = x
      break
  if not xlarge:
    r = x
print(-1)
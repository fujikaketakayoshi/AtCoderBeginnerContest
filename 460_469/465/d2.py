import sys
input = sys.stdin.readline

T = int(input())
# T = 1

for _ in range(T):
  x, y, k = map(int, input().split())
  xs = [x]
  while x != 0:
    x //= k
    xs.append(x)
  
  ys = [y]
  while y != 0:
    y //= k
    ys.append(y)
  
  # print(xs)
  # print(ys)
  l = 0
  r = 0
  while xs[l] != ys[r]:
    if xs[l] > ys[r]:
      l += 1
    else:
      r += 1
  print(l + r)
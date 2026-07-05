import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  x, y, k = map(int, input().split())
  ans = 0
  while x != y:
    if x < y:
      x, y = y, x
    x //= k
    ans += 1
  print(ans)

import sys
input = sys.stdin.readline

T = int(input())
T = 1

for _ in range(T):
  X, Y, K = map(int, input().split())
  
  x = X
  y = x // K
  print(y)
  x = y
  y1 = x // K
  # x = y // K
  y2 = x * K
  y3 = y2 + K - 1
  # y2 = K * x
  print(y1, y2, y3)
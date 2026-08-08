import sys
input = sys.stdin.readline
import math

T = int(input())
# print(T)

for _ in range(T):
  X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
  d1 = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
  d2 = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
  
  # print(d2, (R1 + R2)**2)
  # print(d1 <= R1 + R2)
  # print(d2 <= (R1 + R2)**2)
  # print(max(R1, R2) - d <= min(R1, R2))
  print('Yes' if (d2 <= (R1 + R2) ** 2) and (max(R1, R2) - d1 <= min(R1, R2)) else 'No')


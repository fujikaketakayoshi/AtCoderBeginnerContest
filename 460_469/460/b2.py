import sys
input = sys.stdin.readline

T = int(input())
# print(T)

for _ in range(T):
  X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
  d2 = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
  
  print('Yes' if (d2 <= (R1 + R2) ** 2) and (d2 >= (R1 - R2) ** 2) else 'No')


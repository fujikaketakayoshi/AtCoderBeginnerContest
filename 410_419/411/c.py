import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
# print(N,Q,A)

# 端っこに番兵の白を置く
block = [0] * (N + 2)
num = 0
for a in A:
  if block[a] == 1:
    block[a] = 0
    # 白になる際に
    # 隣接が両方黒+1
    if (block[a - 1] == 1 and block[a + 1] == 1):
      num += 1
    # 隣接がいずれか黒だったら0
    elif (block[a - 1] == 0 and block[a + 1] == 1) or (block[a - 1] == 1 and block[a + 1] == 0):
      1
    # 隣接が両方白だったら-1
    elif (block[a - 1] == 0 and block[a + 1] == 0):
      num -= 1
  else:
    block[a] = 1
    # 黒になる際に
    # 隣接が両方白だったら+1
    if (block[a - 1] == 0 and block[a + 1] == 0):
      num += 1
    # 隣接がいずれか黒だったら0
    elif (block[a - 1] == 1 and block[a + 1] == 0) or (block[a - 1] == 0 and block[a + 1] == 1):
      1
    # 隣接が両方黒だったら-1
    elif block[a - 1] == 1 and block[a + 1] == 1:
      num -= 1
  print(num)
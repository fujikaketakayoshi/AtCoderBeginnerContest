import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
# print(N,Q,A)

# 端っこに番兵の白を置く
block = [0] * (N + 2)
num = 0
for a in A:
  if block[a]:
    num -= (block[a-1] == 0)
    num += (block[a+1] == 1)
  else:
    num += (block[a-1] == 0)
    num -= (block[a+1] == 1)
  block[a] ^= 1
  print(num)
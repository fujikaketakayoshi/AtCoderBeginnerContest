import sys
input = sys.stdin.readline

T = int(input())
# T = 1

for _ in range(T):
  N = int(input())
  S = input().strip()
  X = list(map(int, input().split()))
  Y = list(map(int, input().split()))
  # print(N, S, X, Y)
  
  if S[0] == 'S':
    dpS = 0
    dpR = -X[0]
  else:
    dpS = -X[0]
    dpR = 0
  # print(dpS, dpR)
  
  for i in range(1, N):
    if S[i] == 'S':
      costS = 0
      costR = -X[i]
    else:
      costS = -X[i]
      costR = 0
    ndpS = max(dpS + costS, dpR + costS + Y[i - 1])
    ndpR = max(dpS + costR, dpR + costR)
    dpS = ndpS
    dpR = ndpR
  
  print(max(dpS, dpR))
  
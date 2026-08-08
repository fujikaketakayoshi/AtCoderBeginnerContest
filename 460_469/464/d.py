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
      ndpS = max(dpS, dpR + Y[i - 1])
      ndpR = max(dpS - X[i], dpR - X[i])
    else:
      ndpS = max(dpS - X[i], dpR - X[i] + Y[i - 1])
      ndpR = max(dpS, dpR)
    dpS = ndpS
    dpR = ndpR
  
  print(max(dpS, dpR))
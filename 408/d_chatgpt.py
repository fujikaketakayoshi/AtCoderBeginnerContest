import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  S = input().strip()
  # print(N, S)
  dp0 = 0
  dp1 = float('INF')
  dp2 = float('INF')
  for i in range(N):
    if S[i] == '1':
      ndp0 = dp0 + 1
      ndp1 = min(dp0, dp1)
      ndp2 = min(dp1, dp2) + 1
    else:
      ndp0 = dp0
      ndp1 = min(dp0, dp1) + 1
      ndp2 = min(dp1, dp2)
    dp0 = ndp0
    dp1 = ndp1
    dp2 = ndp2
    print(dp0, dp1, dp2)
  
  print(min(dp0, dp1, dp2))
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
  N, W = map(int, input().split())
  C = list(map(int, input().split()))
  # print(N, W, C) 
  
  min_cost = float('INF')
  for x in range(1, 3 * W + 1):
    cost = 0
    for i in range(1, N + 1):
      if (i + x) % (2 * W) < W:
        cost += C[i - 1]
    # print(i, cost)
    min_cost = min(min_cost, cost)
  print(min_cost)

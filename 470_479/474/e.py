import sys
input = sys.stdin.readline

T = int(input())
# print(T)
# T = 1

for _ in range(T):
  N = int(input())
  
  ABs = []
  discs = []
  prices = []
  buy_idx = set()
  ans = 0
  for i in range(N):
    A, B = map(int, input().split())
    ABs.append((A, B))
    prices.append((A, i))
    discs.append((A - B, i))
  prices.sort(reverse=True)
  discs.sort(reverse=True)
  coupon = False
  while prices or discs:
    # print(prices)
    # print(discs)
    # print(buy_idx)
    if not coupon and prices and not prices[-1][1] in buy_idx:
      p, pi = prices.pop()
      buy_idx.add(pi)
      ans += p
      coupon = True
    elif not coupon and prices:
      prices.pop()
    
    if coupon and discs and not discs[-1][1] in buy_idx:
      d, di = discs.pop()
      buy_idx.add(di)
      ans += ABs[di][1]
      coupon = False
    elif coupon and discs:
      discs.pop()
    
    if len(buy_idx) == N:
      break
  print(ans)
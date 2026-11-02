import sys
input = sys.stdin.readline

S = input().strip()
Q = int(input())
K = list(map(int, input().split()))
# print(S, Q, K)

N = len(S)

ans = []
for k in K:
  k -= 1
  q = k // N
  r = k % N
  
  cnt = 0
  while q > 0:
    cnt += q % 2
    q //= 2
  # print(k, cnt)
  
  c = S[r]
  if cnt % 2:
    c = c.swapcase()
  ans.append(c)
print(' '.join(ans))
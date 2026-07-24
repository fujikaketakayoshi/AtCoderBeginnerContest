import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# print(N, K)
MOD = 10 ** 9

A = [1] * K
Asum = K
for i in range(K, N + 1):
  A.append(Asum)
  new = A[-1]
  old = A[-K - 1]
  Asum = (Asum + new - old) % MOD
  
print(A[-1] % MOD)
      

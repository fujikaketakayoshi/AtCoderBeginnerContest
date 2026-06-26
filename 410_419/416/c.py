import sys
input = sys.stdin.readline
import math

N, K, X = map(int, input().split())
print(N, K, X)

Ss = []
for _ in range(N):
  Ss.append(input().strip())

Ss.sort()
print(Ss)

all = N ** K
print(all)

k = K
i = 0
ans = [0] * (K + 1)
while k > 0:
  kaijou = N ** k 
  if X - kaijou >= 0:
    shou = X // kaijou
    X -= kaijou * shou
    print(k, shou, kaijou, X)
    ans[k] = shou
  k -= 1
  print(ans)


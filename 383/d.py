import sys
input = sys.stdin.readline
import math

N = int(input())
# print(N)
RN = math.isqrt(N)
# print(RN)

# MAX = 4 * 10 ** 12
# RMAX = math.isqrt(MAX)
# print(RMAX)

# 36 => 1, 36, 2, 18, 3,12, 4, 9, 6^2
# 100 => 1, 100, 2, 50, 4, 25, 5, 20, 10^2
# 196 => 1*196, 2*98, 4*49, 7*28, 14*14
# 400 => 1*400, 2*200, 4*100, 8*50, 16*25, 20*20
# 128 => 1*128, 2*64, 4*32, 8*16
# 256 => 1*256, 2*128, 4*64, 8*32, 16*16
# 1000 => 1,1000,10,100

def prime_factors(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

# print(prime_factors(16))


ans = 0
for n in range(1, RN + 1):
  arr = prime_factors(n)
  if len(arr.keys()) == 2 and all(v == 1 for v in arr.values()):
    # print(n, arr)
    ans += 1
  elif len(arr.keys()) == 1 and all(v == 4 for v in arr.values()):
    # print('4', n, arr)
    ans += 1

print(ans)
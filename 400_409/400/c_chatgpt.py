import sys
input = sys.stdin.readline
from math import isqrt

N = int(input())

ans = 0
xa = 2
while xa <= N:
    limit = isqrt(N // xa)
    ans += (limit + 1) // 2
    xa *= 2

print(ans)

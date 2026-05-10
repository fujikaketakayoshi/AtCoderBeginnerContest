import sys
input = sys.stdin.readline
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

def ok(x):
    cnt = 0
    for i, a in enumerate(A, start=1):
        if a < x:
            #cnt += (x - a + i - 1) // i
            cnt += (x - a) // i
            if (x - a) % i != 0:
                cnt += 1
            # cnt += math.ceil((x-a)/i)
        if cnt > K:
            return False
    return True

lo = min(A)
hi = 10**18 + K * N + 1

while hi - lo > 1:
    mid = (lo + hi) // 2
    if ok(mid):
        lo = mid
    else:
        hi = mid

print(lo)
import sys
import bisect
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

# prefix sum
pre = [0] * (N + 1)
for i in range(N):
    pre[i+1] = pre[i] + A[i]

# suffix sum
suf = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    suf[i] = suf[i+1] + A[i]

print(pre, suf, A)
ans = 0

for y in B:
    # A[i] >= y となる最小の i
    x = bisect.bisect_left(A, y)

    # 左側 (A[i] < y)
    left = y * x - pre[x]

    # 右側 (A[i] >= y)
    right = suf[x] - y * (N - x)

    ans = (ans + left + right) % MOD

print(ans)
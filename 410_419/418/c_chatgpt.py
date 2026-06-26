import sys
import bisect
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# 累積和
S = [0]
for a in A:
    S.append(S[-1] + a)

mx = A[-1]

for _ in range(Q):
    b = int(input())

    # そもそも不可能
    if mx < b:
        print(-1)
        continue

    k = b - 1

    idx = bisect.bisect_left(A, b)

    # Ai < b の総和
    small = S[idx]

    # Ai >= b は全部 k
    large = (N - idx) * k

    print(small + large + 1)
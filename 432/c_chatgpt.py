import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

d = Y - X

L = -10**30
R = 10**30

r = (A[0] * X) % d

for a in A:
    if (a * X) % d != r:
        print(-1)
        exit()

    L = max(L, a * X)
    R = min(R, a * Y)

if L > R:
    print(-1)
    exit()

W = R - (R - r) % d

if W < L:
    print(-1)
    exit()

ans = 0
for a in A:
    ans += (W - a * X) // d

print(ans)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [M + 1] * (M + 2)

for _ in range(N):
    L, R = map(int, input().split())
    A[L] = min(A[L], R)

ans = 0
minr = M + 1

for l in range(M, 0, -1):
    minr = min(minr, A[l])
    ans += minr - l

print(ans)
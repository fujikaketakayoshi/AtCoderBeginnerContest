import sys
input = sys.stdin.readline

N, K = map(int, input().split())

M = 1 << N
base = K // M
rem = K % M

A = [base] * M
U = 0


def dfs(l, r, rem):
    global U
    if r - l == 1:
        A[l] += rem
        return rem

    mid = (l + r) // 2
    left = rem // 2
    right = rem - left

    s1 = dfs(l, mid, left)
    s2 = dfs(mid, r, right)

    U = max(U, abs(s1 - s2))
    return s1 + s2


dfs(0, M, rem)

print(U)
print(*A)
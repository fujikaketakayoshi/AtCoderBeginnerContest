import sys
input = sys.stdin.readline


def sol(a, b, c):
    # ax^2 + bx + c = 0 の正の整数解を二分探索
    l = 0
    r = 600_000_001

    while r - l > 1:
        mid = (l + r) // 2

        if a * mid * mid + b * mid + c <= 0:
            l = mid
        else:
            r = mid

    if a * l * l + b * l + c == 0:
        return l

    return -1


N = int(input())

d = 1

while d * d * d <= N:
    if N % d == 0:
        m = N // d

        # 3k^2 + 3dk + d^2 - m = 0
        k = sol(3, 3 * d, d * d - m)

        if k > 0:
            print(k + d, k)
            exit()

    d += 1

print(-1)
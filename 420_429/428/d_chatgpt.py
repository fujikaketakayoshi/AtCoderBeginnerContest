import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    C, D = map(int, input().split())
    ans = 0

    min_digit = len(str(C + 1))
    max_digit = len(str(C + D))

    for k in range(min_digit, max_digit + 1):
        low = 10 ** (k - 1)
        high = 10 ** k - 1

        # x の範囲
        L = max(1, low - C)
        R = min(D, high - C)

        if L > R:
            continue

        base = C * (10 ** k + 1)

        left_val = base + L
        right_val = base + R

        print(right_val, left_val, math.isqrt(right_val), math.isqrt(left_val - 1))
        cnt = math.isqrt(right_val) - math.isqrt(left_val - 1)
        ans += cnt

    print(ans)
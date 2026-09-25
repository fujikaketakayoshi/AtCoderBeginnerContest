import sys
input = sys.stdin.readline

L, R = map(int, input().split())
# print(L, R)

def count_snake(X):
    if X <= 0:
        return 0

    s = str(X)
    n = len(s)
    ans = 0

    # Xより桁数が少ないヘビ数
    for length in range(1, n):
        for first in range(1, 10):
            ans += first ** (length - 1)

    first = int(s[0])

    # Xと同じ桁数だが、先頭がXより小さい
    for d in range(1, first):
        ans += d ** (n - 1)

    # 先頭をXと同じにして、後ろを調べる
    for i in range(1, n):
        d = int(s[i])

        # この桁でXより小さくする
        # 使える数字は 0 ～ first-1
        smaller = min(d, first)

        remain = n - i - 1

        ans += smaller * (first ** remain)

        # X自身のこの桁がfirst以上なら、
        # これ以上Xと同じprefixを辿れない
        if d >= first:
            return ans

    # 最後まで来た = X自身もヘビ数
    ans += 1

    return ans


print(count_snake(R) - count_snake(L - 1))
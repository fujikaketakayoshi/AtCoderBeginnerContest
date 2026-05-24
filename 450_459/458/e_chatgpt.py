import sys

input = sys.stdin.readline

MOD = 998244353

X1, X2, X3 = map(int, input().split())

# 最大値
N = X1 + X2 + X3 + 5

# factorial
fact = [1] * N
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD

# inverse factorial
invfact = [1] * N
invfact[-1] = pow(fact[-1], MOD - 2, MOD)

for i in range(N - 1, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD


def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


ans = 0

# i = 1を置く隙間数
for i in range(1, min(X1, X2 + 1) + 1):

    # X1をi個の非空グループへ
    ways1 = comb(X1 - 1, i - 1)

    # 1を置く隙間を選ぶ
    choose1 = comb(X2 + 1, i)

    rem = X2 + 1 - i

    # j = 3を置く隙間数
    for j in range(1, min(X3, rem) + 1):

        # X3をj個の非空グループへ
        ways3 = comb(X3 - 1, j - 1)

        # 残りから3用隙間選択
        choose3 = comb(rem, j)

        ans += ways1 * ways3 % MOD * choose1 % MOD * choose3
        ans %= MOD

print(ans)
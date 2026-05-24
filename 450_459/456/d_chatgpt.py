import sys
input = sys.stdin.readline

MOD = 998244353
S = input().strip()

dp = [0, 0, 0]  # a,b,c

for ch in S:
    a, b, c = dp

    if ch == 'a':
        dp[0] = (dp[0] + 1 + b + c) % MOD
    elif ch == 'b':
        dp[1] = (dp[1] + 1 + a + c) % MOD
    else:
        dp[2] = (dp[2] + 1 + a + b) % MOD

print(sum(dp) % MOD)
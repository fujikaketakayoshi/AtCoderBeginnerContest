import sys
input = sys.stdin.readline

MOD = 998244353
S = input().strip()

ans = 1
k = 1   # 現在の「交互に続いている長さ」

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        k += 1
    else:
        k = 1
    ans += k

print(ans % MOD)
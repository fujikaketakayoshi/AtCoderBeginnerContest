import sys
input = sys.stdin.readline

N, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

print(AB)

dp = [-1] * (W + 1)
dp[0] = 0

for a, b in AB:
    for w in range(W, b - 1, -1):
        if dp[w - b] != -1:
            dp[w] = max(dp[w], dp[w - b] + a)
    print(dp)

print(max(dp))

# 問題の制約からWが最大10**9なので、dp配列を作るとメモリ制限に引っかかる。
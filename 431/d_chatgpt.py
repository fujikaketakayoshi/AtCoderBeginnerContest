import sys
input = sys.stdin.readline

N = int(input())

items = []
totalB = 0
totalW = 0

for _ in range(N):
    W, H, B = map(int, input().split())
    totalB += B
    totalW += W
    items.append((W, H - B))

maxW = totalW // 2

# dp[w]: 重さwで得られる最大価値
dp = [-10**18] * (maxW + 1)
dp[0] = 0

for W, diff in items:
    for w in range(maxW, W - 1, -1):
        dp[w] = max(dp[w], dp[w - W] + diff)

# 最大値を取る
best = max(dp)

print(totalB + best)
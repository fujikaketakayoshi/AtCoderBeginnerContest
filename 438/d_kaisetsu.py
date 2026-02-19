import sys
input = sys.stdin.readline

INF = 10**18

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# dp[i][j]
# i 個目まで見て
# j = 0,1,2,3 の状態
# 0: まだ何も使ってない
# 1: A区間
# 2: B区間
# 3: C区間

dp = [[-INF]*4 for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    # Aを使う（j=0 or 1 から）
    for j in range(0, 2):
        dp[i+1][1] = max(dp[i+1][1], dp[i][j] + a[i])
    
    # Bを使う（j=1 or 2 から）
    for j in range(1, 3):
        dp[i+1][2] = max(dp[i+1][2], dp[i][j] + b[i])
    
    # Cを使う（j=2 or 3 から）
    for j in range(2, 4):
        dp[i+1][3] = max(dp[i+1][3], dp[i][j] + c[i])

print(dp[n][3])


import sys
import bisect
input = sys.stdin.readline

N = int(input())
P = [0] * N
A = [0] * N
B = [0] * N
for i in range(N):
    P[i], A[i], B[i] = map(int, input().split())

Q = int(input())
X = [0] * Q
for i in range(Q):
    X[i] = int(input())

# DPの最大値を 1000 に拡張
# (500以下の状態から A_i が足されても最大 1000 にしか到達しないため)
MAX_V = 1000
dp = [[0] * (MAX_V + 1) for _ in range(N + 1)]

# ベースケース
for v in range(MAX_V + 1):
    dp[N][v] = v
    
# 後ろからDPを埋める
for i in range(N - 1, -1, -1):
    p, a, b = P[i], A[i], B[i]
    for v in range(MAX_V + 1):
        if v <= p:
            next_v = v + a
            # 1000を超えることはない（500以下に最大500を足すため）
            dp[i][v] = dp[i+1][next_v]
        else:
            next_v = max(v - b, 0)
            dp[i][v] = dp[i+1][next_v]

# クエリ処理のための準備
prefB = [0] * (N + 1)
for i in range(N):
    prefB[i+1] = prefB[i] + B[i]

out = []
for x in X:
    # 1. 最初から500以下なら、0番目のプレゼントからDPに丸投げ
    if x <= 500:
        out.append(str(dp[0][x]))
        continue

    # 2. 最後まで500以下に落ちないケース
    if x - prefB[N] > 500:
        out.append(str(x - prefB[N]))
        continue
        
    # 3. 途中で500以下になるインデックス i を探す
    # prefB[i] >= x - 500 となる最初の i
    target = x - 500
    i = bisect.bisect_left(prefB, target)
    
    # i番目のプレゼントを見る直前に、初めて500以下になる
    v_at_i = x - prefB[i]
    
    # DPテーブルから答えを取得
    out.append(str(dp[i][v_at_i]))

print('\n'.join(out) + '\n')
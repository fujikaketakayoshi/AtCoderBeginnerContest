import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    S = [input().strip() for _ in range(H)]

    INF = 10**9
    dp = [ [INF] * (1 << W) for _ in range(H) ]

    # maskがその行で可能か
    def valid_mask(row, mask):
        for j in range(W):
            if (mask >> j) & 1:
                if S[row][j] == '.':
                    return False
        return True

    # コスト（消した数）
    def cost(row, mask):
        c = 0
        for j in range(W):
            if S[row][j] == '#' and ((mask >> j) & 1) == 0:
                c += 1
        return c

    # 初期化
    for mask in range(1 << W):
        if valid_mask(0, mask):
            dp[0][mask] = cost(0, mask)
    print(dp[0])

    # 遷移
    for i in range(1, H):
        for prev in range(1 << W):
            if dp[i-1][prev] == INF:
                continue
            for curr in range(1 << W):
                if not valid_mask(i, curr):
                    continue

                ok = True
                for j in range(W - 1):
                    if (
                        (prev >> j) & 1 and
                        (prev >> (j+1)) & 1 and
                        (curr >> j) & 1 and
                        (curr >> (j+1)) & 1
                    ):
                        ok = False
                        break

                if not ok:
                    continue

                dp[i][curr] = min(
                    dp[i][curr],
                    dp[i-1][prev] + cost(i, curr)
                )
    print(dp)
    print(min(dp[H-1]))
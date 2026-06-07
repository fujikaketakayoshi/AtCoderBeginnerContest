import sys
input = sys.stdin.readline

H, W, K = map(int, input().split())
S = [input().strip() for _ in range(H)]

# 縦方向累積和
col = [[0] * W for _ in range(H + 1)]

for i in range(H):
    row = S[i]
    for j in range(W):
        col[i + 1][j] = col[i][j] + (row[j] == '1')


def subp(B, K):
    n = len(B)

    r1 = 0   # 初めて >= K となる位置
    r2 = 0   # 初めて > K となる位置

    res = 0

    for l in range(n - 1):

        if r1 < l + 1:
            r1 = l + 1
        if r2 < l + 1:
            r2 = l + 1

        while r1 < n and B[r1] - B[l] < K:
            r1 += 1

        while r2 < n and B[r2] - B[l] <= K:
            r2 += 1

        res += r2 - r1

    return res


ans = 0

for top in range(H):
    for bottom in range(top, H):

        # B[0]=0
        B = [0] * (W + 1)

        for j in range(W):
            x = col[bottom + 1][j] - col[top][j]
            B[j + 1] = B[j] + x

        ans += subp(B, K)

print(ans)

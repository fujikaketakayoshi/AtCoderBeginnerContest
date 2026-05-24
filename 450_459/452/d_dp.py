import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

m = len(T)

# dp[j]:
# 現在位置を右端とする部分文字列で
# Tの先頭j文字を部分列として含み
# j+1文字目はまだ含まない個数
dp = [0] * (m + 1)

ans = 0

for ch in S:
    # 新しく1文字部分文字列を開始
    dp[0] += 1

    # ch と一致する T の位置を後ろから更新
    for j in range(m - 1, -1, -1):
        if ch == T[j]:
            dp[j + 1] += dp[j]
            dp[j] = 0

    # T全体を含まないものだけ加算
    ans += sum(dp[:m])
    # 以下だとT全体を含む部分文字列の数になる
    # ans += dp[m]

print(ans)
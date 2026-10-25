import sys
input = sys.stdin.readline
from functools import cmp_to_key

# 偏角ソート用の比較関数
def compare(a, b):
    ax, ay = a
    bx, by = b

    # 上半分を先にする
    ha = 0 if ay > 0 or (ay == 0 and ax > 0) else 1
    hb = 0 if by > 0 or (by == 0 and bx > 0) else 1

    if ha != hb:
        return ha - hb

    # 外積で角度の大小を判定
    cross = ax * by - ay * bx

    if cross > 0:
        return -1
    else:
        return 1


T = int(input())

for _ in range(T):
    N = int(input())

    P = []
    for _ in range(N):
        X, Y = map(int, input().split())
        P.append((X, Y))

    # 偏角ソート
    P.sort(key=cmp_to_key(compare))

    # 円環を2周分に展開
    P = P + P

    ans = 0
    r = 0

    # しゃくとり法
    for l in range(N):
        if r < l:
            r = l

        ax, ay = P[l]

        while r + 1 < l + N:
            bx, by = P[r + 1]

            cross = ax * by - ay * bx

            if cross <= 0:
                break

            r += 1

        ans = max(ans, r - l + 1)

    print(ans)

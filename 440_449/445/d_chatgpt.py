import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())

h = [0] * N
w = [0] * N
for i in range(N):
    h[i], w[i] = map(int, input().split())

# 高さ降順インデックス
ord_h = sorted(range(N), key=lambda i: -h[i])

# 幅降順インデックス
ord_w = sorted(range(N), key=lambda i: -w[i])

used = [False] * N
ans_x = [0] * N
ans_y = [0] * N

ih = 0
iw = 0

for _ in range(N):
    # 使用済みは飛ばす（ここは合計でN回しか進まない）
    while used[ord_h[ih]]:
        ih += 1
    while used[ord_w[iw]]:
        iw += 1

    # 今置くピースを決める
    if h[ord_h[ih]] == H:
        i = ord_h[ih]
    else:
        i = ord_w[iw]

    # 右下に置く
    ans_x[i] = H - h[i] + 1
    ans_y[i] = W - w[i] + 1

    used[i] = True

    # 残りサイズ更新
    if h[i] == H:
        W -= w[i]
    else:
        H -= h[i]

for i in range(N):
    print(ans_x[i], ans_y[i])

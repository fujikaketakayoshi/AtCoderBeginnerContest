import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# up[x]   : x の上にあるカード (なければ 0)
# down[x] : x の下にあるカード (なければ 0)
up = [0] * (N + 1)
down = [0] * (N + 1)

# pile_id[x] : 「x がその山の頂上であるとき」その山番号
# （頂上カードから山番号がわかる）
pile_id = [0] + [i for i in range(1, N + 1)]

# size[i] : 山 i の枚数
size = [0] + [1] * N

# bottom[i] : 山 i の一番下のカード
bottom = [0] + [i for i in range(1, N + 1)]

for _ in range(Q):
    C, P = map(int, input().split())

    # P は必ず山の頂上
    to_pile = pile_id[P]

    # C を含む山の頂上まで登って元の山を特定
    cur = C
    while up[cur] != 0:
        cur = up[cur]
    from_top = cur
    from_pile = pile_id[from_top]

    # C以上の枚数を数える
    cnt = 0
    cur = C
    while cur != 0:
        cnt += 1
        cur = up[cur]

    # C の下側を切断
    below = down[C]
    if below != 0:
        up[below] = 0
        pile_id[below] = from_pile  # 残った山の新しい頂上
    else:
        # 元山が空になる
        bottom[from_pile] = 0

    # P の上に C を接続
    up[P] = C
    down[C] = P

    # 移動後の山の新しい頂上は元山の頂上
    pile_id[from_top] = to_pile

    # 枚数更新
    size[from_pile] -= cnt
    size[to_pile] += cnt

print(*size[1:])
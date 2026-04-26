import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# 各山の枚数
deck_nums = [0] + [1] * N

# card_next[x][0] = x の上にあるカード
# card_next[x][1] = x の下にあるカード
card_next = [[0, 0] for _ in range(N + 1)]

# card_index[x] = カード x が属する山番号
card_index = [0] + [i for i in range(1, N + 1)]

for _ in range(Q):
    C, P = map(int, input().split())

    # C の元の山
    pre_index = card_index[C]

    # P の山
    next_index = card_index[P]

    # C の下にいるカード
    below = card_next[C][1]

    # C以上のカード枚数を数えつつ、
    # 所属山を next_index に更新
    card_num = 0
    cur = C
    while cur != 0:
        card_index[cur] = next_index
        card_num += 1
        cur = card_next[cur][0]

    # 元山から C を切り離す
    if below != 0:
        card_next[below][0] = 0
    card_next[C][1] = P

    # P の上に C を接続
    card_next[P][0] = C

    # 枚数更新
    deck_nums[pre_index] -= card_num
    deck_nums[next_index] += card_num

print(*deck_nums[1:])
import sys
input = sys.stdin.readline

N, R, C = map(int, input().split())
S = input().strip()

DIR = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}

# 現在までの風による累積移動量
r, c = 0, 0

# 過去に登場した累積座標
seen = {(0, 0)}

ans = []

for ch in S:
    dr, dc = DIR[ch]
    r += dr
    c += dc

    # 過去に P_t - (R, C) が登場していれば、
    # その時点で発生した煙が現在 (R, C) にいる
    if (r - R, c - C) in seen:
        ans.append('1')
    else:
        ans.append('0')

    seen.add((r, c))
    print(seen)
    print(r - R, c - C)

print(''.join(ans))
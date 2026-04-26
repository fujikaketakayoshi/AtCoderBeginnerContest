import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# 0-indexed にする
# 実カード: 0 ... N-1
# 仮想カード: N ... 2N-1

up = [-1] * (2 * N)
down = [-1] * (2 * N)

# 初期状態：
# 仮想カード(N+i) の上に 実カード(i) が1枚乗っている
for i in range(N):
    up[N + i] = i
    down[i] = N + i

for _ in range(Q):
    C, P = map(int, input().split())
    C -= 1
    P -= 1

    # C の下にあるカード（仮想カード含む）
    D = down[C]

    # C以上を P の上に移動
    down[C] = P
    up[P] = C

    # 元の山を切断
    up[D] = -1

# 各山の枚数を数える
ans = []

for i in range(N):
    x = N + i
    cnt = 0

    while up[x] != -1:
        x = up[x]
        cnt += 1

    ans.append(cnt)

print(*ans)
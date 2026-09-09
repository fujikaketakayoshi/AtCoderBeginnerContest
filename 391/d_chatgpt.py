import sys
input = sys.stdin.readline

N, W = map(int, input().split())

blocksW = [[] for _ in range(W + 1)]

for i in range(N):
    X, Y = map(int, input().split())
    blocksW[X].append((Y, i + 1))

for w in range(1, W + 1):
    blocksW[w].sort()

# 消せる段数
eraseH = min(len(blocksW[w]) for w in range(1, W + 1))

INF = 10**18
eraseTime = [INF] * (N + 1)

for h in range(eraseH):
    # h段目が消える時刻
    t = 0

    for w in range(1, W + 1):
        t = max(t, blocksW[w][h][0])

    # この段に属する全ブロックは同時に消える
    for w in range(1, W + 1):
        block_id = blocksW[w][h][1]
        eraseTime[block_id] = t

Q = int(input())

for _ in range(Q):
    T, A = map(int, input().split())

    print('Yes' if T < eraseTime[A] else 'No')
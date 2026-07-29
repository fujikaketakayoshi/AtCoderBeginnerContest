import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

H, W = map(int, input().split())

A = []
for _ in range(H):
    A.extend(map(int, input().split()))

N = H * W

ans = 0

def dfs(mask, x):
    global ans

    if mask == (1 << N) - 1:
        ans = max(ans, x)
        return

    # 一番左上(番号が小さい)未処理マス
    for i in range(N):
        if (mask >> i) & 1 == 0:
            break
    
    print(mask, i, x)
    # このマスを残す
    dfs(mask | (1 << i), x ^ A[i])

    y = i // W
    z = i % W

    # 右にドミノ
    if z + 1 < W:
        j = i + 1
        if (mask >> j) & 1 == 0:
            dfs(mask | (1 << i) | (1 << j), x)

    # 下にドミノ
    if y + 1 < H:
        j = i + W
        if (mask >> j) & 1 == 0:
            dfs(mask | (1 << i) | (1 << j), x)

dfs(0, 0)
print(ans)
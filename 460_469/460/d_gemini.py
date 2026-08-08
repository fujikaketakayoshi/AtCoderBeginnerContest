import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# 8近傍の方向
DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# --- ステップ1: 1回操作を行う ---
next_grid = [['.'] * W for _ in range(H)]

for y in range(H):
    for x in range(W):
        if grid[y][x] == '#':
            # 元が黒のマス自体は白（.）になるが、その周囲の白を黒にする
            for dy, dx in DIR:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W:
                    if grid[ny][nx] == '.':
                        next_grid[ny][nx] = '#'

# グリッドを1手進めたものに更新
grid = next_grid

# --- ステップ2: 多始点BFSで最短距離を求める ---
# 解説の「infを偶数にする」を真似て、十分に大きい偶数を初期値にする
INF = 10**9
dist = [[INF] * W for _ in range(H)]
q = deque()

# 1手進めた世界で黒（#）のマスを始点とする
for y in range(H):
    for x in range(W):
        if grid[y][x] == '#':
            dist[y][x] = 0
            q.append((y, x))

while q:
    y, x = q.popleft()
    
    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if dist[ny][nx] == INF:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
print(dist)


# --- ステップ3: 残り手数が奇数回の反転を考慮して出力 ---
for y in range(H):
    ans = []
    for x in range(W):
        # 距離が偶数なら '.' 、奇数なら '#'
        # 初期状態が全て白/黒で一度も黒が発生しなかった場合、distはINF（偶数）のままなので正しく '.' になる
        if dist[y][x] % 2 == 0:
            ans.append('.')
        else:
            ans.append('#')
    print(''.join(ans))

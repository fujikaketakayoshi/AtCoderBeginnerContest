import sys
from collections import deque

input_data = sys.stdin.read().split()
H, W = int(input_data[0]), int(input_data[1])
grid_str = input_data[2:]

is_black = [[False] * W for _ in range(H)]
cnt = [[0] * W for _ in range(H)]

# 現在のステップで「新たに黒くなった」マスを管理する
# 初期状態の黒マスをセット
current_blacks = []
ans = 0
for r in range(H):
    for c in range(W):
        if grid_str[r][c] == '#':
            is_black[r][c] = True
            current_blacks.append((r, c))
            ans += 1

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while current_blacks:
    changed_whites = set()
    for r, c in current_blacks:
        for dr, dc in DIR:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and not is_black[nr][nc]:
                cnt[nr][nc] += 1
                changed_whites.add((nr, nc))
    
    next_blacks = []
    for r, c in changed_whites:
        if cnt[r][c] == 1:
            is_black[r][c] = True
            next_blacks.append((r, c))
            ans += 1

    current_blacks = next_blacks

print(ans)

import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
grid = []
start = goal = None

for i in range(H):
    row = input().strip()
    grid.append(row)
    for j, c in enumerate(row):
        if c == 'S':
            start = (i, j)
        elif c == 'G':
            goal = (i, j)

# print(grid)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dc = "URDL"

visited = [[[False] * 4 for _ in range(W)] for _ in range(H)]
parent = [[[-1] * 4 for _ in range(W)] for _ in range(H)]

q = deque()
sy, sx = start

for d in range(4):
    q.append((sy, sx, d))
    visited[sy][sx][d] = True

goal_state = None

while q:
    y, x, last = q.popleft()

    if (y, x) == goal:
        goal_state = (y, x, last)
        break

    cell = grid[y][x]

    if cell == 'o':
        dirs = [last]
    elif cell == 'x':
        dirs = [d for d in range(4) if d != last]
    else:
        dirs = range(4)

    for d in dirs:
        ny = y + dy[d]
        nx = x + dx[d]

        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if grid[ny][nx] == '#':
            continue
        if visited[ny][nx][d]:
            continue

        visited[ny][nx][d] = True
        parent[ny][nx][d] = last
        q.append((ny, nx, d))

if goal_state is None:
    print("No")
    exit()

# 経路復元
y, x, d = goal_state
path = []

while (y, x) != start:
    path.append(dc[d])
    py = y - dy[d]
    px = x - dx[d]
    d = parent[y][x][d]
    y, x = py, px

path.reverse()

print("Yes")
print(''.join(path))
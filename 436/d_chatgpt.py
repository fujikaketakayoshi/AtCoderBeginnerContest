from collections import deque, defaultdict

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

warp = defaultdict(list)
for i in range(H):
    for j in range(W):
        if grid[i][j].islower():
            warp[grid[i][j]].append((i, j))

dist = [[-1]*W for _ in range(H)]
dist[0][0] = 0

q = deque([(0,0)])
used_warp = set()

while q:
    y, x = q.popleft()
    
    if (y, x) == (H-1, W-1):
        print(dist[y][x])
        exit()
    
    # ワープ
    c = grid[y][x]
    if c.islower() and c not in used_warp:
        used_warp.add(c)
        for ny, nx in warp[c]:
            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    
    # 4方向
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny, nx = y+dy, x+dx
        if 0<=ny<H and 0<=nx<W and grid[ny][nx] != '#' and dist[ny][nx]==-1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny,nx))

print(-1)
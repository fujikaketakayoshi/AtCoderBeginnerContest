import sys
input = sys.stdin.readline
from collections import deque,defaultdict

H, W = map(int, input().split())
grid = []
warp = defaultdict(list)
for h in range(H):
  row = list(input().strip())
  grid.append(row)
  for w, r in enumerate(row):
    if r.islower():
      warp[r].append((h, w))
# print(warp)

visited = [[False] * W for _ in range(H)]
used_warp = set()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()
q.append((0, 0, 0))
visited[0][0] = True
min_cost = float('INF')
while q:
  c, h, w = q.popleft()
  if h == H - 1 and w == W - 1:
    print(c)
    sys.exit()
  # print(h, w, c)
  key = grid[h][w]
  if key.islower() and key not in used_warp:
    used_warp.add(key)
    for nh, nw in warp[key]:
      if nh == h and nw == w:
        continue
      if not visited[nh][nw]:
        q.append((c + 1, nh, nw))
        visited[nh][nw] = True
        continue
  
  for d in range(4):
    nh = h + dy[d]
    nw = w + dx[d]
    if not (0 <= nh <= H - 1) or not (0 <= nw <= W - 1):
      continue
    if grid[nh][nw] == '#' or visited[nh][nw]:
      continue
    q.append((c + 1, nh, nw))
    visited[nh][nw] = True

print(-1)
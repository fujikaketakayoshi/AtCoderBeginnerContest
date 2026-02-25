import sys
input = sys.stdin.readline
from collections import defaultdict
import heapq

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

hq = []
heapq.heappush(hq, (0, 0, 0))
visited[0][0] = True
min_cost = float('INF')
while hq:
  if min_cost != float('INF'):
    break
  c, h, w = heapq.heappop(hq)
  if h == H - 1 and w == W - 1:
    min_cost = min(min_cost, c)
    break
  # print(h, w, c)
  key = grid[h][w]
  if key.islower() and key not in used_warp:
    used_warp.add(key)
    for nh, nw in warp[key]:
      if nh == h and nw == w:
        continue
      if not visited[nh][nw]:
        heapq.heappush(hq, (c + 1, nh, nw))
        visited[nh][nw] = True
        continue
  
  for d in range(4):
    nh = h + dy[d]
    nw = w + dx[d]
    if not (0 <= nh <= H - 1) or not (0 <= nw <= W - 1):
      continue
    if grid[nh][nw] == '#' or visited[nh][nw]:
      continue
    heapq.heappush(hq, (c + 1, nh, nw))
    visited[nh][nw] = True

print(-1 if min_cost == float('INF') else min_cost)
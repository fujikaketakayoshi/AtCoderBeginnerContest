import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import math

N = int(input())
# print(H, W, N, Q)

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
# print(graph)

C = list(map(int, input().split()))
# print(C)

q = deque()
q.append(1)

dist = [-1] * (N + 1)
dist[1] = 0
dist_max = -1
dist_max_u1 = -1
while q:
  u = q.popleft()
  for v in graph[u]:
    if dist[v] != -1:
      continue
    dist[v] = dist[u] + 1
    if dist_max < dist[v]:
      dist_max = dist[v]
      dist_max_u1 = v
    q.append(v)
# print(dist, dist_max_u1)

q = deque()
q.append(dist_max_u1)
dist = [-1] * (N + 1)
dist[dist_max_u1] = 0
dist_max = -1
dist_max_u2 = -1
parent = [-1] * (N + 1)
while q:
  u = q.popleft()
  for v in graph[u]:
    if dist[v] != -1:
      continue
    parent[v] = u
    dist[v] = dist[u] + 1
    if dist_max < dist[v]:
      dist_max = dist[v]
      dist_max_u2 = v
    q.append(v)
# print(dist, dist_max_u2)
# print(dist_max, dist_max_u1, dist_max_u2)
# print(parent)

path = []
u = dist_max_u2
while u != -1:
    path.append(u)
    u = parent[u]
path.reverse()
# print(path)
if len(path) % 2 == 0: # 辺が中心の場合
  center1 = path[dist_max // 2]
  center2 = path[dist_max // 2 + 1]
  # print(center1, center2)
  r = dist_max // 2
  q = deque()
  q.append(center1)
  dist = [-1] * (N + 1)
  dist[center1] = 0
  # r == 0 の場合は中心の頂点のみが距離 r にある
  center1path = [center1] if r == 0 else []
  while q:
    u = q.popleft()
    for v in graph[u]:
      if v == center2 or dist[v] != -1:
        continue
      dist[v] = dist[u] + 1
      if dist[v] == r:
        center1path.append(v)
      q.append(v)
  q = deque()
  q.append(center2)
  dist = [-1] * (N + 1)
  dist[center2] = 0
  # r == 0 の場合は中心の頂点のみが距離 r にある
  center2path = [center2] if r == 0 else []
  while q:
    u = q.popleft()
    for v in graph[u]:
      if v == center1 or dist[v] != -1:
        continue
      dist[v] = dist[u] + 1
      if dist[v] == r:
        center2path.append(v)
      q.append(v)
  # print(center1path, center2path)
  colors1 = defaultdict(int)
  for u in center1path:
    colors1[C[u - 1]] += 1
  colors2 = defaultdict(int)
  for u in center2path:
    colors2[C[u - 1]] += 1
  # print(colors1, colors2)
  ans = 0
  for c, cnt in colors1.items():
    ans += cnt * colors2[c]
  print(ans)
else: # 頂点が中心の場合
  center = path[dist_max // 2]
  # print(center)
  r = dist_max // 2
  q = deque()
  q.append(center)
  dist = [-1] * (N + 1)
  dist[center] = 0
  branch = [-1] * (N + 1)
  centerpath = []
  while q:
    u = q.popleft()
    for v in graph[u]:
      if dist[v] != -1:
        continue
      dist[v] = dist[u] + 1
      if u == center:
        branch[v] = v
      else:
        branch[v] = branch[u]
      if dist[v] == r:
        centerpath.append(v)
      q.append(v)
  # print(centerpath)
  # print(branch)
  colors = defaultdict(int)
  branch_colors = defaultdict(int)
  for u in centerpath:
    c = C[u - 1]
    b = branch[u]
    colors[c] += 1
    branch_colors[(b, c)] += 1
  # print(colors)
  # print(branch_colors)
  ans = 0
  for cnt in colors.values():
    ans += math.comb(cnt, 2)
  for cnt in branch_colors.values():
    ans -= math.comb(cnt, 2)
  print(ans)

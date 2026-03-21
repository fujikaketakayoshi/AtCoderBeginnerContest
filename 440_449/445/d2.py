import sys
input = sys.stdin.readline
import heapq

H, W, N = map(int, input().split())

h_hq = []
w_hq = []

pre_H = H
pre_W = W
used_index = set()
order_index = []
P = []

for i in range(N):
  h, w = map(int, input().split())
  P.append((h, w))
  heapq.heappush(h_hq, (-h, w, i))
  heapq.heappush(w_hq, (-w, h, i))

while h_hq or w_hq:
  while h_hq and (-h_hq[0][0] == pre_H or h_hq[0][2] in used_index):
    p = heapq.heappop(h_hq)
    if not p[2] in used_index:
      used_index.add(p[2])
      order_index.append(p[2])
      pre_W -= p[1]
  while w_hq and (-w_hq[0][0] == pre_W or w_hq[0][2] in used_index):
    p = heapq.heappop(w_hq)
    if not p[2] in used_index:
      used_index.add(p[2])
      order_index.append(p[2])
      pre_H -= p[1]

print(order_index)
h, w = 0, 0
pre_H, pre_W = H, W
ans = [[] for _ in range(N)]
for idx in order_index:
  y, x = P[idx]
  ans[idx] = (h + 1, w + 1)
  if y == pre_H:
    pre_W -= x
    w += x
  elif x == pre_W:
    pre_H -= y
    h += y

for a, b in ans:
  print(a, b)

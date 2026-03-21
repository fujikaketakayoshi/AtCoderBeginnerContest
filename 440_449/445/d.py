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

for i in range(N):
  h, w = map(int, input().split())
  heapq.heappush(h_hq, (-h, w, i))
  heapq.heappush(w_hq, (-w, h, i))

while h_hq or w_hq:
  print(pre_H, pre_W, h_hq, w_hq)
  while -h_hq[0][0] == pre_H:
    p = heapq.heappop(h_hq)
    if not p[2] in used_index:
      used_index.add(p[2])
      order_index.append(p[2])
      pre_W -= p[1]
  while -w_hq[0][0] == pre_W:
    p = heapq.heappop(w_hq)
    if not p[2] in used_index:
      used_index.add(p[2])
      order_index.append(p[2])
      pre_H -= p[1]

print(order_index)
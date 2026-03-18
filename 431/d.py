import sys
input = sys.stdin.readline

N = int(input())
# print(N)

Ws = []
totalBW, totalhappy = 0, 0
for _ in range(N):
  W, H, B = map(int, input().split())
  totalBW += W
  totalhappy += B
  Ws.append((H - B, W, H, B))

Ws.sort(reverse=True)
# print(Ws)
totalHW = 0
for (diff, W, H, B) in Ws:
  if diff > 0 and totalBW - W >= totalHW + W:
    totalhappy += diff
    totalHW += W
    totalBW -= W
print(totalhappy)
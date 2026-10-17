import sys
input = sys.stdin.readline

N, W = map(int, input().split())
# print(N, W)

AB = []
for _ in range(N):
  A, B = map(int, input().split())
  AB.append((A, B))
# print(AB)

ans = 0
for S in range(1 << N):
  w = 0
  y = 0
  ok = True
  for i in range(N):     # 各ビットを見る
    if (S >> i) & 1:   # i番目のビットが1なら
      y += AB[i][0]
      w += AB[i][1]
      if w > W:
        ok = False
        break
  if ok:
    ans = max(ans, y)

print(ans)
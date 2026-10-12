import sys
input = sys.stdin.readline

N, W = map(int, input().split())
# print(N, W)

AB = []
for _ in range(N):
  A, B = map(int, input().split())
  AB.append((A, B))
# print(AB)

def subsets_bit(N):
    points = list(range(1, N + 1))
    subsets = []

    for S in range(1 << N):     # 0 ~ 7
        subset = []
        for i in range(N):     # 各ビットを見る
            if (S >> i) & 1:   # i番目のビットが1なら
                subset.append(points[i])
        subsets.append(subset)
    return subsets

ans = 0
for ss in subsets_bit(N):
  w = 0
  y = 0
  ok = True
  for s in ss:
    i = s - 1
    y += AB[i][0]
    w += AB[i][1]
    if w > W:
      ok = False
      break
  if ok:
    ans = max(ans, y)

print(ans)
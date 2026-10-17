import sys
input = sys.stdin.readline

Q, V = map(int, input().split())
# print(Q, V)

bats = []
idxs = set()
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    t = query[1]
    w = query[2]
    bats.append([t, w])
  else:
    idx = None
    t = query[1]
    ans = 0
    for i, tw in enumerate(bats):
      if i in idxs:
        continue
      ts, w = tw
      if ans < w + (t - ts):
        ans = w + (t - ts)
        idx = i
    if idx != None:
      idxs.add(idx)
    ans = min(V, ans)
    print(-1 if ans == 0 else ans)

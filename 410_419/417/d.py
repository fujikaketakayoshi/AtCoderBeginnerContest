import sys
input = sys.stdin.readline
import bisect

N = int(input())
# print(N)
MAX = 500

pab = []
presumB = [0] * (N + 1)
for i in range(N):
  P, A, B = map(int, input().split())
  pab.append((P, A, B))
  presumB[i + 1] = presumB[i] + B
# print(presumB)

threshold = []
for i, (p,a,b) in enumerate(pab):
    threshold.append(p + presumB[i])

dp = [0] * (MAX + 1)
for x in range(MAX + 1):
  tmpx = x
  for p, a, b in pab:
    if tmpx <= p:
      tmpx += a
    else:
      tmpx = max(tmpx - b, 0)
  dp[x] = tmpx
# print(dp)

Q = int(input())
# print(Q)
for _ in range(Q):
  X = int(input())
  if X >= MAX:
    idx = bisect.bisect_left(threshold, X)

    if idx == len(threshold):
        print(X - presumB[-1])
        continue

    cur = X - presumB[idx]
    cur += pab[idx][1]

    for i in range(idx + 1, N):
        if cur <= pab[i][0]:
            cur += pab[i][1]
        else:
            cur = max(cur - pab[i][2], 0)

    print(cur)
  else:
    print(dp[X])

import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
  N = int(input().strip())
  deers = []
  for _ in range(N):
    W, P = map(int, input().split())
    deers.append((W, P))
  deers.sort(key=lambda x: x[1], reverse=True)
  sumW = [0] * (N + 1)
  for i in range(1, N + 1):
    sumW[i] = sumW[i - 1] + deers[i - 1][0]
  power = 0
  ok = False
  for i in range(N):
    power += deers[i][1]
    weight = sumW[N] - sumW[i + 1]
    if power >= weight:
      print(N - (i + 1))
      ok = True
      break
  if not ok:
    print(0)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Mset = set(range(1, M + 1))

for _ in range(N):
  L = int(input().strip())
  X = list(map(int, input().split()))
  ok = False
  for x in X:
    if x in Mset:
      Mset.remove(x)
      ok = True
      print(x)
      break
  if not ok:
    print(0)

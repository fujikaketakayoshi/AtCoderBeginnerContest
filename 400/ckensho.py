import sys
input = sys.stdin.readline
from collections import defaultdict

N = 400

MAX = 10 ** 18

cnt = defaultdict(list)
beki = []

for a in range(1, MAX):
  Xa = 2 ** a
  if Xa > N:
    break
  beki.append(a)

for b in range(1, 10 ** 9):
  Xb = b ** 2
  if Xb > N:
    break
  for a in beki:
    X = 2 ** a * Xb
    if X > N:
      break
    cnt[X].append((a, b))


for k, v in cnt.items():
  if len(v) > 1:
    print(k, v)


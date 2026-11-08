import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
# print(N, M)

vote1s = [0] * (N + 1)

vote2s = [defaultdict(int) for _ in range(N + 1)]

for _ in range(M):
  A, B = map(int, input().split())
  # print(A, B)
  vote1s[A] += 1
  vote2s[A][B] += 1

vote1t = []
for i, v in enumerate(vote1s):
  vote1t.append((v, i))


sorted_vote1t = sorted(vote1t, key=lambda t: (-t[0], t[1]))
first = sorted_vote1t[0]
second = sorted_vote1t[1]

for k in range(1, N + 1):
  if first[1] == k:
    vmax = second[0]
    top = second[1]
  else:
    vmax = first[0]
    top = first[1]
  for i, v in vote2s[k].items():
    if vmax < vote1s[i] + v:
      vmax = vote1s[i] + v
      top = i
    elif vmax == vote1s[i] + v:
      top = min(top, i)
  print(top)
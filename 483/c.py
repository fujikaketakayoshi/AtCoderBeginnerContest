import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
print(N, M)

vote1s = [0] * (N + 1)

vote2s = [defaultdict(int) for _ in range(N + 1)]

for _ in range(M):
  A, B = map(int, input().split())
  print(A, B)
  vote1s[A] += 1
  vote2s[A][B] += 1

vote1t = []
for i, v in enumerate(vote1s):
  vote1t.append((v, i))

vote1t.sort(reverse=True)

vote2t = []
for vs in vote2s:
  vst = sorted(vs.items(), key=lambda x: x[1], reverse=True)
  vote2t.append(vst)

print(vote1t)
print(vote2t)

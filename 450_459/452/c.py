import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = []
B = []
for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

M = int(input())
S = []
cnt = [[defaultdict(int) for _ in range(11)] for _ in range(11)]

for _ in range(M):
  s = input().strip()
  S.append(s)
  ns = len(s)
  for i, c in enumerate(s):
    cnt[ns][i + 1][c] += 1

for s in S:
  ns = len(s)
  if ns != N:
    print('No')
    continue
  ok = True
  i = 0
  while i < ns:
    if not s[i] in cnt[A[i]][B[i]]:
      ok = False
      break
    i += 1
  print('Yes' if ok else 'No')

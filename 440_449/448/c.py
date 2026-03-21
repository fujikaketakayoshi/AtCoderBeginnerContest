import sys
input = sys.stdin.readline
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1
setA = set(sorted(A))

for _ in range(Q):
  K = int(input())
  B = list(map(int, input().split()))
  tmpcnt = cnt.copy()
  tmpsetA = setA.copy()
  for b in B:
    val = A[b - 1]
    tmpcnt[val] -= 1
    if tmpcnt[val] == 0:
      tmpsetA.remove(val)
  print(list(tmpsetA)[0])

import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

B = []
cnt = defaultdict(int)
for i in range(N):
  idx = -1
  if A[i] in cnt:
    idx = cnt[A[i]]
  cnt[A[i]] = i + 1
  B.append(idx)

print(*B)
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1

uniqueA = []
for k, v in cnt.items():
  if v == 1:
    uniqueA.append(k)

if not uniqueA:
  print(-1)
  exit()

maxuniA = max(uniqueA)
for i in range(N):
  if A[i] == maxuniA:
    print(i + 1)
    exit()


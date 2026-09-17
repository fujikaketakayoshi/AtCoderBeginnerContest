import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

cnt1 = defaultdict(int)
cnt2 = defaultdict(int)

cnt1[A[0]] += 1
for i in range(1, N):
  cnt2[A[i]] += 1


# print(cnt1)
# print(cnt2)

ans = len(cnt1.keys()) + len(cnt2.keys())
# print(ans)

for i in range(1, N - 1):
  cnt1[A[i]] += 1
  cnt2[A[i]] -= 1
  if cnt2[A[i]] == 0:
    del cnt2[A[i]]
  ans = max(ans, len(cnt1.keys()) + len(cnt2.keys()))

print(ans)
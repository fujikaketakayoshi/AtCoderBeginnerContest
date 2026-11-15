import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

cnt = defaultdict(int)
for a in A:
  cnt[a] += 1
# print(cnt)

ans = N * (N - 1) // 2
# print(ans)

for i in range(N-1,-1,-1):
  cnt[A[i]] -= 1
  ans -= cnt[A[i]]
print(ans)
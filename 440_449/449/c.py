import sys
input = sys.stdin.readline
from collections import defaultdict

N, L, R = map(int, input().split())
S = input().strip()
# print(N, L, R)
# print(S)

ans = 0
i = 0
j = i + L
while j < N:
  while j < N and L <= j - i <= R:
    # print(i, j, S[i], S[j], j - i)
    if S[i] == S[j]:
      ans += 1
    j += 1
  i += 1
  j = i + L
print(ans)

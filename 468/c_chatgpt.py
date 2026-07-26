import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
# print(N, P, Q)

arr = list(range(1, N + 1))
ans = 0
for p in permutations(arr, N):
  if P < p < Q:
    ans += 1
print(ans)
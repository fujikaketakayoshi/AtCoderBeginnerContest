import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
# print(N, P, Q)

arr = list(range(1, N + 1))
ans = 0
for p in list(permutations(arr, N)):
  p = list(p)
  if p > P and p < Q:
    ans += 1
print(ans)
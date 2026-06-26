import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)

ans = 0

for j in range(N):
    ans += cnt[j - A[j]]
    cnt[j + A[j]] += 1

print(ans)
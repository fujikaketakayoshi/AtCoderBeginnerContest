import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
C = list(map(int, input().split()))
# print(N, C)
ans = [0] * N
l = 0

while l < N:
    r = l

    # 同じ色が続く限りrを進める
    while r + 1 < N and C[r + 1] == C[l]:
        r += 1

    # 区間[l, r]が確定
    for i in range(l, r + 1):
        left = i - l + 1 if l > 0 else N
        right = r - i + 1 if r < N - 1 else N
        ans[i] = min(left, right)

    # 次の区間へ
    l = r + 1

print(*ans)
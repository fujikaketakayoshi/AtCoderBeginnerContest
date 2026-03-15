from collections import defaultdict
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
S = input().strip()

cnt = defaultdict(list)
for i, c in enumerate(S):
    cnt[c].append(i)

ans = 0

for pos in cnt.values():
    l = r = 0
    for i in range(len(pos)):
        while l < len(pos) and pos[l] < pos[i] + L:
            l += 1
        while r < len(pos) and pos[r] <= pos[i] + R:
            r += 1
        ans += max(0, r - l)

print(ans)
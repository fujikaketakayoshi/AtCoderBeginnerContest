import sys
input = sys.stdin.readline
from collections import defaultdict

N, M, C = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for a in A:
    cnt[a] += 1

positions = sorted(cnt.keys())
K = len(positions)
counts = [cnt[p] for p in positions]

# 2周分
pos2 = positions + [p + M for p in positions]
cnt2 = counts + counts

prefix = [0] * (2 * K + 1)
for i in range(2 * K):
    prefix[i+1] = prefix[i] + cnt2[i]

ans = 0
r = 0
running_sum = 0

for l in range(K):
    if r < l:
        r = l
        running_sum = 0
    while r < 2 * K and running_sum < C:
        running_sum += cnt2[r]
        r += 1
    
    # Xi = prefix[r] - prefix[l]
    xi = prefix[r] - prefix[l]
    
    # スタート区間の長さ: (直前の座標, positions[l]] の幅
    prev = positions[l - 1] if l > 0 else positions[K - 1] - M
    interval_len = positions[l] - prev
    
    ans += xi * interval_len
    running_sum -= cnt2[l]

print(ans)

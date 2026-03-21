import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input().strip())
n = int(N ** 0.5)

cnt = defaultdict(int)

for y in range(1, n + 1):
    y2 = y * y
    for x in range(1, y):
        cand = x * x + y2
        if cand > N:
            break
        cnt[cand] += 1

ans = []
for k, v in cnt.items():
    if v == 1:
        ans.append(k)
ans.sort()
print(len(ans))
print(*ans)

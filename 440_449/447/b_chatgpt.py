import sys
input = sys.stdin.readline
from collections import Counter

S = input().strip()

cnt = Counter(S)
max_cnt = max(cnt.values())

ans = ''.join(c for c in S if cnt[c] != max_cnt)

print(ans)

import sys
from collections import defaultdict
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

cnt0 = defaultdict(int)
cnt1 = defaultdict(int)
cnt2 = defaultdict(int)

for _ in range(N):
    S = input().strip()
    cnt0[S] += 1

    for i in range(M):
        tmp = S[:i] + '*' + S[i+1:]
        cnt1[tmp] += 1

    for i, j in combinations(range(M), 2):
        tmp = list(S)
        tmp[i] = '*'
        tmp[j] = '*'
        cnt2[''.join(tmp)] += 1

def count_pairs(cnt):
    return sum(v * (v - 1) // 2 for v in cnt.values())

A0 = count_pairs(cnt0)
A1 = count_pairs(cnt1)
A2 = count_pairs(cnt2)

print(A0, cnt0)
print(A1, cnt1)
print(A2, cnt2)

ans = A2 - (M - 2) * A1
ans += (M - 1) * (M - 2) // 2 * A0

print(ans)

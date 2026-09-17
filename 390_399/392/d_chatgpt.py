import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())

dice = []

for _ in range(N):
    q = list(map(int, input().split()))
    K, A = q[0], q[1:]
    dice.append((K, Counter(A)))

ans = 0.0

for i in range(N):
    for j in range(i + 1, N):
        ki, cnti = dice[i]
        kj, cntj = dice[j]

        same = 0

        for v, c in cnti.items():
            same += c * cntj.get(v, 0)

        prob = same / (ki * kj)
        ans = max(ans, prob)

print(ans)
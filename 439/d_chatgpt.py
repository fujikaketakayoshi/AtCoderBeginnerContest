import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt7 = defaultdict(int)
cnt5 = defaultdict(int)
cnt3 = defaultdict(int)

# 全体カウント
for v in A:
    if v % 7 == 0:
        cnt7[v // 7] += 1
    if v % 5 == 0:
        cnt5[v // 5] += 1
    if v % 3 == 0:
        cnt3[v // 3] += 1

left7 = defaultdict(int)
left3 = defaultdict(int)

ans = 0

for v in A:
    if v % 5 == 0:
        x = v // 5

        l7 = left7[x]
        l3 = left3[x]

        r7 = cnt7[x] - l7
        r3 = cnt3[x] - l3

        ans += l7 * l3   # j が最大
        ans += r7 * r3   # j が最小

    if v % 7 == 0:
        left7[v // 7] += 1
    if v % 3 == 0:
        left3[v // 3] += 1

print(ans)

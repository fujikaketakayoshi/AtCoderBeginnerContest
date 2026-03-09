import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

def intlen(x):
    return len(str(x))

cnt = defaultdict(int)

for a in A:
    cnt[(intlen(a), a % M)] += 1

ans = 0

for a in A:
    for l in range(1, 11):
        x = a * pow(10, l) % M
        need = 0 if x == 0 else M - x
        # need = (M - x) % M
        ans += cnt[(l, need)]

print(ans)
import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

def intlen(x):
    lx = 0
    while x > 0:
        lx += 1
        x //= 10
    return lx

# (len, mod) ごとの個数
cnt = defaultdict(int)

lens = set()

for a in A:
    la = intlen(a)
    cnt[(la, a % M)] += 1
    lens.add(la)

ans = 0
for a in A:
    for l in lens:
        mod1 = (a * pow(10, l)) % M
        need = (M - mod1) % M
        ans += cnt[(l, need)]

print(ans)
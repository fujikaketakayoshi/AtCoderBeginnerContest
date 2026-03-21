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

# Ai % M の個数
cnt2 = defaultdict(int)
for a in A:
    cnt2[a % M] += 1

# Ajの桁数
lA = set()
for a in A:
    lA.add(intlen(a))

# 10^k % M
pow10 = {}
for l in lA:
    pow10[l] = pow(10, l, M)

ans = 0

for a in A:
    for l in lA:
        mod1 = (a * pow10[l]) % M
        need = (M - mod1) % M
        ans += cnt2[need]

print(ans)
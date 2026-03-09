import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def intlen(x):
  lx = 0
  while x > 0:
    lx += 1
    x //= 10
  return lx

lmaxA = intlen(A[-1])

lA = set()
for a in A:
  lA.add(intlen(a))

cnt1 = defaultdict(lambda: defaultdict(list))
cnt2 = defaultdict(list)
for a in A:
  la = intlen(a)
  mod2 = a % M
  cnt2[mod2].append(a)
  for l in lA:
    val = a * 10 ** (la + l - 1)
    mod1 = val % M
    lval = intlen(val)
    cnt1[mod1][lval].append(val)

ans = 0
for mod, xs in cnt2.items():
  mod2 = M - mod if M - mod != 0 else 0
  for x in xs:
    lx = intlen(x)
    ans += len(cnt1[mod2][lx + 1])

print(ans)
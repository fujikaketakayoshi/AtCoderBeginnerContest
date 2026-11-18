import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

total = M * (M + 1) // 2
# print(total)

LRs = []
imos = [0] * (M + 2)
one = 0
for _ in range(N):
  L, R = map(int, input().split())
  if L == R:
    one += 1
  else:
    LRs.append((L, R))
    imos[L] += 1
    imos[R + 1] -= 1
LRs.sort()
# print(imos)

S = [0] * (M + 2)
for i in range(M + 1):
  S[i + 1] = S[i] + imos[i + 1]
# print(S)

Sr = []
Sr_l = set()
pre = S[0]
for i, s in enumerate(S[1:]):
  if s >= 1 and pre == 0:
    l = i + 1
    pre = 1
  elif s >= 1 and pre == 1:
    continue
  elif s == 0 and pre == 1:
    Sr.append((l, i))
    Sr_l.add(l)
    pre = 0
# print(Sr)
# print(Sr_l)

ex = 0
inc = 0
for l, r in Sr:
  if l in Sr_l:
    ex += (r - l + 1) * (r - l) // 2

minl = 2 * 10 ** 5 + 1
maxr = 0
for l, r in LRs:
  if not l in Sr_l:
    if l > maxr:
      inc += (r - l + 1) * (r - l) // 2
    elif r < maxr:
      continue
    else:
      l = maxr
      inc += (r - l + 1) * (r - l) // 2
    maxr = r
    # print((l,r), (r - l + 1) * (r - l) // 2)

# print(ex, inc)

print(total - ex + inc - one)
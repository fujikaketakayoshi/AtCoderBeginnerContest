import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
S = input().strip()
# print(N, S)

cnt = defaultdict(int)
for s in S:
  cnt[s] += 1
# print(cnt)


precnt = defaultdict(int)
preabc = set()
preok = False
l = 0
for s in S:
  l += 1
  precnt[s] += 1
  cnt[s] -= 1
  preabc.add(s)
  if 'A' in preabc and 'B' in preabc and 'C' in preabc:
    preok = True
    break
# print(precnt)

sufcnt = defaultdict(int)
sufabc = set()
sufok = False
r = N - 1
for s in reversed(S):
  r -= 1
  sufcnt[s] += 1
  cnt[s] -= 1
  sufabc.add(s)
  if 'A' in sufabc and 'B' in sufabc and 'C' in sufabc:
    sufok = True
    break
# print(sufcnt)
# print(cnt)

cntok = True
for v in cnt.values():
  if v <= 0:
    cntok = False

if not (preok and sufok and cntok):
  print(0)
  exit()

# print(l, r)
ans = 1
tmpcnt = cnt.copy()
for ri in range(r, l + 1, -1):
  tmpcnt[S[ri]] -= 1
  if tmpcnt[S[ri]] == 0:
    break
  ans += 1

tmpcnt = cnt.copy()
for li in range(l, r + 1):
  tmpcnt[S[li]] -= 1
  if tmpcnt[S[li]] == 0:
    break
  ans += 1
  pretmpcnt = tmpcnt.copy()
  for ri in range(r, l + 1, -1):
    tmpcnt[S[ri]] -= 1
    if tmpcnt[S[ri]] == 0:
      break
    ans += 1
  tmpcnt = pretmpcnt.copy()

print(ans)
  
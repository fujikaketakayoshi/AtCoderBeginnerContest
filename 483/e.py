import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
print(N, M)

Ss = []
for _ in range(N):
  S = input().strip()
  Ss.append(S)
print(Ss)

fS = {}
cnt0 = defaultdict(int)
cnt1 = defaultdict(int)
cnt2 = defaultdict(int)
for S in Ss:
  fS[S] = {}
  cnt0[S] += 1
  for i in range(M):
    tmp = S[:i] + '*' + S[i + 1:]
    cnt1[tmp] += 1
    fS[S][tmp] = {}

for j in range(i + 1, M):
# fS.append(tmp[:j] + '*' + tmp[j + 1:])
  tmp2 = tmp[:j] + '*' + tmp[j + 1:]
  cnt2[tmp2] += 1
  fS[S][tmp][tmp2] = {}

print(fS)
print(cnt0)
print(cnt1)
print(cnt2)

ans = 0
for k0 in fS.keys():
  if cnt0[k0] >= 2:
    print('k0', k0)
    for k1 in fS[k0].keys():
      cnt1[k1] -= cnt0[k0] - 1
    ans += cnt0[k0] - 1

for k0 in fS.keys():
  print('fS[k0].keys()', fS[k0].keys(), k0)
  for k1 in fS[k0].keys():
    if cnt1[k1] >= 2:
      print('k1,keys', k1, fS[k0])
      for k2 in fS[k0][k1].keys():
        print('k1-k2', k2)
        cnt2[k2] -= cnt1[k1] - 1 
      ans += cnt1[k1] - 1
      cnt1[k1] = 1
print(cnt2)
for k0 in fS.keys():
  for k1 in fS[k0].keys():
    for k2 in fS[k0][k1].keys():
      if cnt2[k2] >= 2:
        print('k2', k2)
        ans += cnt2[k2] - 1

print(ans)
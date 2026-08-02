import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

AB = set()
for _ in range(M):
  A, B = map(int, input().split())
  AB.add((A, B))

if len(AB) == 1:
  print(1)
  exit()

ABs = []
for A, B in AB:
  ABs.append((A, B))

A1, B1 = ABs[0]
A2, B2 = ABs[1]

combs = []
if A1 != A2:
  combs.append(set([A1, A2]))
if A1 != B2:
  combs.append(set([A1, B2]))
if B1 != A2:
  combs.append(set([B1, A2]))
if B1 != B2:
  combs.append(set([B1, B2]))
# print(combs)

for i in range(2, len(ABs)):
  Ai, Bi = ABs[i]
  # print(Ai, Bi)
  n = len(combs)
  rm_idx = []
  for j in range(n):
    if Ai in combs[j]:
      1
    elif Bi in combs[j]:
      1
    else:
      rm_idx.append(j)
  for idx in reversed(rm_idx):
    combs.pop(idx)
print(len(combs))
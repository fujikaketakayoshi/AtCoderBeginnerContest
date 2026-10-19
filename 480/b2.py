import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

Ss = []
for _ in range(N):
  S = input().strip()
  Ss.append(S)

Scnt = [0] * N
for _ in range(M):
  T = input().strip()
  ok = False
  cands = []
  for j, S in enumerate(Ss):
    if S == T:
      Scnt[j] += 1
      ok = True
      break
    if len(S) != len(T):
      continue
    cnt = 0
    for i in range(len(S)):
      if S[i] != T[i]:
        cnt += 1
    if cnt == 1:
      cands.append(j)

  if not ok and len(cands) == 1:
    Scnt[cands[0]] += 1

for c in Scnt:
  print(c)
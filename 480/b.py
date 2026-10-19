import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

Ss = []
for _ in range(N):
  S = input().strip()
  Ss.append(S)

Ts = []
for _ in range(M):
  T = input().strip()
  Ts.append(T)

Scnt = [0] * N
for T in Ts:
  ok = None
  Scnt2 = [0] * N
  for j, S in enumerate(Ss):
    if len(S) != len(T):
      continue
    elif S == T:
      ok = j
      break
    cnt = 0
    for i in range(len(S)):
      if S[i] != T[i]:
        cnt += 1
    # print(S, T, cnt)
    if cnt == 1:
      Scnt2[j] += 1
  # print(T)
  # print('ok',ok)
  
  if ok is None:
    cnt2cnt = 0
    for v in Scnt2:
      if v == 1:
        cnt2cnt += 1
    if cnt2cnt == 1:
      for k in range(len(Scnt2)):
        if Scnt2[k] == 1:
          ok = k
  if ok is not None:
    Scnt[ok] += 1

# print(Scnt)
for c in Scnt:
  print(c)
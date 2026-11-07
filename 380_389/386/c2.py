import sys
input = sys.stdin.readline

K = int(input())
S = input().strip()
T = input().strip()
# print(K, S, T)

NS = len(S)
NT = len(T)

if S == T:
  print('Yes')
  exit()
elif abs(NS - NT) > 1:
  print('No')
  exit()

if NS == NT:
  diff_cnt = 0
  for i in range(NS):
    if S[i] != T[i]:
      diff_cnt += 1
  print('Yes' if diff_cnt == 1 else 'No')
else:
  if NS < NT:
    S, T, NS, NT = T, S, NT, NS
  si = 0
  ti = 0
  diff_cnt = 0
  while ti < NT:
    if S[si] == T[ti]:
      si += 1
      ti += 1
    else:
      if diff_cnt == 1:
        print('No')
        exit()
      diff_cnt += 1
      si += 1
  print('Yes')


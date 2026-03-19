import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
S = input().strip()
# print(N,A,B,S)

i, j = 0, 0
cnta, cntb = 0, 0
prev_j = -1
ans = 0
while i < N:
  if S[i] == 'a':
    cnta += 1
  else:
    cntb += 1
  # print(i, j, cnta, cntb, S[j:i + 1], cnta >= A and cntb < B)
  if cnta == A and cntb < B:
    ans += 1
  elif cnta > A and cntb < B:
    ans += 1
    while j < N and cnta > A:
      # print('2', i, j, cnta, cntb, S[j + 1:i + 1], cnta >= A and cntb < B)
      if S[j] == 'a':
        cnta -= 1
        ans += 1
      else:
        cntb -= 1
      j += 1
  elif cntb >= B:
    while j < N and cntb >= B:
      if S[j] == 'a':
        cnta -= 1
      else:
        cntb -= 1
      j += 1
  i += 1
print(ans)
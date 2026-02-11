import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip())
cnt = 0

for l in range(N):
  a_num = 0
  b_num = 0
  if S[l] == 'A':
    a_num += 1
  elif S[l] == 'B':
    b_num += 1
  if a_num > b_num:
    cnt += 1
  for r in range(l + 1, N):
    if S[r] == 'A':
      a_num += 1
    elif S[r] == 'B':
      b_num += 1
    if a_num > b_num:
      cnt += 1

print(cnt)
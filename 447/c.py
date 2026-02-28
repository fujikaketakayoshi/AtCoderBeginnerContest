import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
# print(S, T)

ls = len(S)
lt = len(T)

cnt = 0
i = 0
j = 0
suc_as = 0
suc_at = 0
while i < ls or j < lt:
  # print(i, j)
  while i < ls and S[i] == 'A':
    i += 1
    suc_as += 1
  
  while j < lt and T[j] == 'A':
    j += 1
    suc_at += 1
  
  if i < ls and j < lt:
    if S[i] == T[j]:
      cnt += abs(suc_as - suc_at)
      i += 1
      j += 1
      suc_as = 0
      suc_at = 0
    else:
      print(-1)
      exit()

cnt += abs(suc_as - suc_at)
print(cnt)
import sys
input = sys.stdin.readline

T = int(input())
MAX = 10 ** 5

for _ in range(T):
  N = int(input())
  S = input().strip()
  # print(N, S)
  if N == 1:
    print(S)
    continue
  
  i = 0
  j = 0
  while i < N - 1:
    ok = False
    if S[i] > S[i + 1]:
      target = S[i]
      j = i
      # print(target, target > S[j + 1])
      while j < N - 1 and target >= S[j + 1]:
        ok = True
        j += 1
    if ok:
      break
    i += 1
  
  # print(i,j)
  if i == N - 1 and j == 0:
    ans = S[:N - 2] + S[-1] + S[-2]
  else:
    ans = S[:i] + S[i+1:j+1] + S[i] + S[j+1:]
  print(ans)
  

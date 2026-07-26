import sys
input = sys.stdin.readline

S = input().strip()
# print(S)

N = len(S)

ans = 0
for i in range(N):
  l = i
  r = i
  wrong_cnt = 0
  while l >= 0 and r < N:
    if S[l] == S[r]:
      ans += 1
    elif S[l] != S[r] and wrong_cnt == 0:
      ans += 1
      wrong_cnt += 1
    else:
      wrong_cnt += 1
    if wrong_cnt >= 2:
      break
    l -= 1
    r += 1
  
  l = i
  r = i + 1
  wrong_cnt = 0
  while l >= 0 and r < N:
    if S[l] == S[r]:
      ans += 1
    elif S[l] != S[r] and wrong_cnt == 0:
      ans += 1
      wrong_cnt += 1
    else:
      wrong_cnt += 1
    if wrong_cnt >= 2:
      break
    l -= 1
    r += 1

print(ans)
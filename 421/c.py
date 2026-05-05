import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip())
# print(N, S)
i = 1
prev = S[0]
succ = 1
cnt = 0
while i < 2 * N:
  if prev == S[i]:
    succ += 1
  elif succ > 1 and prev != S[i]:
    now = i
    i -= succ - 1
    # print(i, now, succ)
    S[i], S[now] = S[now], S[i]
    cnt += succ - 1
    prev = S[i]
    succ = 1
  else:
    prev = S[i]
    succ = 1
  # print(S)
  i += 1
print(cnt)
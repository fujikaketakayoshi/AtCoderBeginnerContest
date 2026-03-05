import sys
input = sys.stdin.readline

S = str(input().strip())

pre = ''
pre_suc = 0
post = ''
post_suc = 0
cnt = 0

i = 0
while i <= len(S) - 1:
  # print(i, pre, pre_suc)
  if pre == '':
    pre = S[i]
    pre_suc += 1
  elif pre == S[i]:
    pre_suc += 1
  elif pre != S[i]:
    if int(pre) + 1 == int(S[i]):
      cnt += 1
      j = 1
      while j < pre_suc and i + j <= len(S) - 1:
        # print(i + j, S[i + j])
        if S[i + j] == S[i]:
          cnt += 1
          j += 1
        else:
          break
    pre = S[i]
    pre_suc = 1
  i += 1

print(cnt)

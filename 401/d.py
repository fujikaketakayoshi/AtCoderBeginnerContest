import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# print(N, K)
S = input().strip()
# print(S)
S = '.' + S + '.'

Xs = []
for i in range(1, N + 1):
  if S[i] == '?':
    if S[i - 1] == 'o' or S[i + 1] == 'o':
      Xs.append('.')
    else:
      Xs.append('?')
  else:
    Xs.append(S[i])
# print(Xs)

def run_length_encoding(seq):
    if not seq:
        return []

    res = []
    prev = seq[0]
    cnt = 1

    for x in seq[1:]:
        if x == prev:
            cnt += 1
        else:
            res.append((prev, cnt))
            prev = x
            cnt = 1

    res.append((prev, cnt))
    return res

# print(Xs)
rleX = run_length_encoding(Xs)
# print(rleX)
cnto = 0
cntqomax = 0
for c, v in rleX:
  if c == 'o':
    cnto += 1
  elif c == '?':
    cntqomax += (v + 1) // 2

T = []
if K - cnto == cntqomax and cntqomax != 0:
  for c, v in rleX:
    if c == '?' and v % 2 == 1:
      for i in range(v):
        T.append('o' if i % 2 == 0 else '.')
    else:
      for _ in range(v):
        T.append(c)
elif K - cnto == 0:
  for c, v in rleX:
    if c == '?':
      for _ in range(v):
        T.append('.')
    else:
      for _ in range(v):
        T.append(c)
else:
  for c, v in rleX:
    for _ in range(v):
      T.append(c)

print(''.join(T))
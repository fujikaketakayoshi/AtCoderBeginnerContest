import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)


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

rleA = run_length_encoding(A)
# print(rleA)

ans = 0
cnt = 0
idx = [-1] * (N + 1)
start_i = 0
for i, t in enumerate(rleA):
  d, c = t
  # print(i,d,c)
  if c >= 2 and cnt == 0:
    idx[d] = i
    start_i = i
    cnt += 1
    ans = max(ans, cnt)
  elif cnt > 0 and c == 2:
    if idx[d] != -1:
      old_i = idx[d]
      cnt = i - old_i
      for j in range(start_i, old_i + 1):
        idx[rleA[j][0]] = -1
      start_i = old_i + 1
    else:
      cnt += 1
    idx[d] = i
    ans = max(ans, cnt)
  elif cnt > 0 and c > 2:
    if idx[d] == -1:
      ans = max(ans, cnt + 1)
    for j in range(start_i, i + 1):
      idx[rleA[j][0]] = -1
    idx[d] = i
    cnt = 1
    start_i = i
  else:
    for j in range(start_i, i + 1):
      idx[rleA[j][0]] = -1
    ans = max(ans, cnt)
    start_i = i
    cnt = 0
print(ans * 2)
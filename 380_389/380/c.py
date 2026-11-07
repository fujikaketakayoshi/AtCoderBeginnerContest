import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()
# print(N, K, S)

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

rleS = run_length_encoding(S)
# print(rleS)

k = 0
idx = -1
for i, t in enumerate(rleS):
  d, c = t
  if d == '1':
    k += 1
  if k == K:
    idx = i
    break

# print(idx)
rleS[idx], rleS[idx - 1] = rleS[idx - 1], rleS[idx]
# print(rleS)

ans = []
for d, c in rleS:
  ans.append(d * c)
print(''.join(ans))
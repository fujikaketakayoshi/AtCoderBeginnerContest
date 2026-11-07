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

B = []
for d, c in rleA:
  if c <= 1:
    B.append(-1)
  elif c == 2:
    B.append(d)
  elif c > 2:
    B.extend([d, -1, d])
# print(B)


used = set()
l = 0
ans = 0

for r, x in enumerate(B):
    if x == -1:
        used.clear()
        l = r + 1
        continue

    while x in used:
        used.remove(B[l])
        l += 1

    used.add(x)
    ans = max(ans, r - l + 1)

print(ans * 2)
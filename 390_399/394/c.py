import sys
input = sys.stdin.readline

S = input().strip()

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
            res.append([prev, cnt])
            prev = x
            cnt = 1

    res.append([prev, cnt])
    return res

rle = run_length_encoding(S)
# print(rle)

ans = []
for i in range(len(rle) - 1):
  if rle[i][0] == 'W' and rle[i + 1][0] == 'A':
    ans.append('A' + 'C' * rle[i][1])
    rle[i + 1][1] -= 1
  else:
    ans.append(rle[i][0] * rle[i][1])

ans.append(rle[-1][0] * rle[-1][1])
print(''.join(ans))

import sys
input = sys.stdin.readline
N = int(input())

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

ans = []
i = 1
while i < N:
  j = i
  while j < N:
    j += 1
    out = '? ' + str(i) + ' ' + str(j)
    print(out, flush=True)
    yn = input().strip()
    if yn == 'Yes':
      ans.append(1)
    else:
      i = j - 1
      ans.append(0)
      break
  i += 1


ans2 = run_length_encoding(ans)
# print(ans2)

cnt = 0
for x in ans2:
  if x[0] == 1:
    cnt += (x[1] - 1) * x[1] // 2
print('! ' + str(cnt))
exit()

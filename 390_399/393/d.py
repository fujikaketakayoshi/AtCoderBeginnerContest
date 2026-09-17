import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
S = input().strip()
# print(N, S)

idxs = []
for i, c in enumerate(S):
  if c == '1':
    idxs.append(i)

# print(idxs)
n = len(idxs)
if n == 1:
  print(0)
  exit()

l = 0
r = n - 1
lcost = 1
rcost = 1
ans = 0
while l < r:
  lnum = (idxs[l + 1] - idxs[l] - 1) * lcost
  rnum = (idxs[r] - idxs[r - 1] - 1) * rcost
  if lnum == rnum and r - l == 1:
    # print('1!', l, r)
    ans += lnum
    l += 1
  elif lnum == rnum:
    # print('2!', l, r)
    ans += lnum + rnum
    l += 1
    r -= 1
  elif lnum < rnum:
    # print('3!', l, r)
    ans += lnum
    lcost += 1
    l += 1
  elif lnum > rnum:
    # print('4!', l, r)
    ans += rnum
    rcost += 1
    r -= 1

print(ans)
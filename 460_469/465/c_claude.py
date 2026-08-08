import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
S = input().strip()

D = deque()
flip = False
for k in range(1, N + 1):
  if flip:
    D.appendleft(k)
  else:
    D.append(k)
  if S[k - 1] == 'o':
    flip = not flip

if flip:
  ans = list(D)[::-1]
else:
    ans = list(D)
print(*ans)

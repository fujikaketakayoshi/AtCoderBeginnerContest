import sys
input = sys.stdin.readline
import bisect

N = int(input())
S = input().strip()

ocnt = [0] * N
xcnt = [0] * N
o = 0
x = 0
for i in range(N):
  if S[i] == 'o':
    o += 1
  else:
    x += 1
  ocnt[i] = o
  xcnt[i] = x
# print(ocnt, xcnt)

for k in range(N):
  idx = bisect.bisect_left(xcnt, ocnt[k] + xcnt[k])
  # print(idx)
  print(N if idx == N else idx + 1)


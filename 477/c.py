import sys
input = sys.stdin.readline
import bisect

Q = int(input())
S = input().strip()
T = input().strip()
# print(Q, S, T)
lenT = len(T)

Tidxs = []
for i in range(len(S) - lenT + 1):
  if S[i:i + lenT] == T:
    Tidxs.append(i)
# print(Tidxs)


for _ in range(Q):
  L, R = map(int, input().split())
  lidx = bisect.bisect_left(Tidxs, L - 1)
  # print(lidx)
  if lidx == len(Tidxs):
    print('No')
    continue
  ridx = Tidxs[lidx] + lenT - 1
  if ridx <= R - 1:
    print('Yes')
  else:
    print('No')
  # print(lidx, Tidxs[lidx] + lenT - 1)
import sys
input = sys.stdin.readline
import bisect

N = int(input())
# print(N)

H = []
L = []
for _ in range(N):
  h, l = map(int, input().split())
  H.append(h)
  L.append(l)
# print(H)
# print(L)

HMAX = []
hmax = 0
for i in range(N - 1, -1, -1):
  hmax = max(hmax, H[i])
  HMAX.append(hmax)
HMAX.reverse()
# print(HMAX)

Q = int(input())
T = list(map(int, input().split()))
# print(Q, T)

for t in T:
  idx = bisect.bisect_right(L, t)
  print(HMAX[idx])

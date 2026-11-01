import sys
input = sys.stdin.readline
import bisect

H, W, N, Q = map(int, input().split())
# print(H, W, N, Q)

Rs = []
Cs = []
for _ in range(N):
  R, C = map(int, input().split())
  Rs.append(R)
  Cs.append(C)
Rs.sort()
Cs.sort()
# print(Rs)
# print(Cs)

for _ in range(Q):
  q, l, r = map(int, input().split())
  # print(q, l, r)
  if q == 1:
    lidx = bisect.bisect_left(Rs, l)
    ridx = bisect.bisect_right(Rs, r)
    # print(q, l, r, lidx, ridx, ridx - lidx)
    print(ridx - lidx)
  else:
    lidx = bisect.bisect_left(Cs, l)
    ridx = bisect.bisect_right(Cs, r)
    # print(q, l, r, lidx, ridx, ridx - lidx)
    print(ridx - lidx)
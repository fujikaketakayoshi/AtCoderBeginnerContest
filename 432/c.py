import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
# print(N, X, Y, A)

A.sort()
tmp_max = A[0] * Y
tmp_min = A[0] * X
d = Y - X
r = (A[0] * X) % d
for a in A:
  if (a * X) % d != r:
    print(-1)
    exit()
  amax = a * Y
  amin = a * X
  # print(tmp_max, tmp_min)
  # (tmp_min, tmp_max), (amin, amax)
  if max(tmp_min, amin) <= min(tmp_max, amax):
    tmp_max = min(tmp_max, amax)
    tmp_min = max(tmp_min, amin)
  else:
    print(-1)
    exit()

cnt = tmp_max // Y
for i in range(1, N):
  xnum = (A[i] * Y - tmp_max) // (Y - X)
  ynum = A[i] - xnum
  cnt += ynum
  # print(xnum, ynum)
print(cnt)
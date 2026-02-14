import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
print(A)

for _ in range(Q):
  X, Y = map(int, input().split())
  idx = bisect.bisect_right(A, X)
  if idx == N:
    ans = X + Y - 1
  else:
    kosuu = A[idx] - X
    pre_num = A[idx]
    while kosuu < Y:
      idx += 1
      if idx == N:
        ans = pre_num + (Y - kosuu)
        break
      elif A[idx] - pre_num - 1 + kosuu < Y:
        kosuu += A[idx] - pre_num - 1
        pre_num = A[idx]
        continue
      else:
        ans += Y - kosuu + pre_num
        break
  print(ans)
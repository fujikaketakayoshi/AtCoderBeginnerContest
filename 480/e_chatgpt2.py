import sys
input = sys.stdin.readline
import math

N = int(input())
# print(N)
sqN = math.isqrt(N)

def prod_num(a, lenA, d):
  l = 1
  if d is None:
    r = sqN + 1
  else:
    r = d
  while l < r:
    mid = (l + r) // 2
    total = 1
    if lenA == 3:
      total = a * (a + mid) * (a + 2 * mid)
    else:
      for i in range(lenA):
        total *= (a + mid * i)
        if total > N:
          break
    # print(l, r, mid, total)
    if total <= N:
      l = mid + 1
    else:
      r = mid
  return l - 1

# print(prod_num(1, 4))
# exit()

ans = 0
for i in range(1, N):
  cnt = 0
  pred = None
  for j in range(3, N):
    cnt2 = prod_num(i, j, pred)
    # print(i, j, cnt2)
    if cnt2 == 0:
      break
    pred = cnt2 + 1
    cnt += cnt2
  if cnt == 0:
    break
  ans += cnt
print(ans)
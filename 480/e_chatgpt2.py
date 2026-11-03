import sys
input = sys.stdin.readline

N = int(input())
# print(N)
cubN = int(N ** (1/3))
sqN = int(N ** (1/2))

def prod_num(a, lenA, d = sqN + 1):
  l = 1
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
for i in range(1, cubN + 2):
  cnt = 0
  pred = None
  for j in range(3, cubN + 2):
    cnt2 = prod_num(i, j, pred)
    # print(i, j, cnt2)
    if cnt2 == 0:
      break
    pred = cnt2
    cnt += cnt2
  if cnt == 0:
    break
  ans += cnt
print(ans)
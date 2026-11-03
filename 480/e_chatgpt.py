import sys
input = sys.stdin.readline

N = int(input())
# print(N)
cubN = int(N ** (1/3))
sqN = int(N ** (1/2))

def prod_num(a, lenA):
  l = 1
  r = sqN + 1
  while l < r:
    mid = (l + r) // 2
    total = 1
    for i in range(lenA):
      total *= (a + mid * i)
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
  ok = True
  cnt = 0
  for j in range(3, cubN + 2):
    cnt2 = prod_num(i, j)
    # print(i, j, cnt2)
    if cnt2 == 0:
      break
    cnt += cnt2
  if cnt == 0:
    break
  ans += cnt
print(ans)
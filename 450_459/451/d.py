import sys
input = sys.stdin.readline

N = int(input())
# print(N)

MAX = 10 ** 9

beki = []
for i in range(0, MAX):
  if 2 ** i > MAX:
    break
  beki.append(2 ** i)
# print(beki, len(beki))

k = 1
ketas = [[] for _ in range(9)]
i = 0
while k < 10:
  while i < 30:
    if beki[i] // (10 ** k) == 0:
      ketas[k - 1].append(beki[i])
      i += 1
    else:
      break
#  print(ketas)
  k += 1

yoi = []
for i in range(0, 9):
  for j in range(0, 9):
    for ki in ketas[i]:
      for kj in ketas[j]:
        yoi.append(int(str(ki) + str(kj)))

ans = sorted(yoi + beki)
print(ans)
print(ans[N - 1])
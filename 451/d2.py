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

yoi = []

def dfs(i):
  yoi.append(i)
  for j in beki:
    v = int(str(i) + str(j))
    if v > MAX:
      break
    dfs(v)

for i in beki:
  dfs(i)

ans = sorted(list(set(yoi)))
print(ans[N - 1])


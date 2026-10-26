import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

r = M - (N - 1) * 10

ans = []
fans = []
def dfs(i):
  # print(ans)
  if i == N:
    fans.append(ans[:])
    return
  pre = ans[-1] + 10
  for n in range(i * 10 + 1, i * 10 + r + 1):
    # print(i, pre, n)
    if pre <= n and n <= M:
      ans.append(n)
      dfs(i + 1)
      ans.pop()

for n in range(1, r + 1):
  ans.append(n)
  dfs(1)
  ans.pop()

print(len(fans))
for f in fans:
  print(*f)

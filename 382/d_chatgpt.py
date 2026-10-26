import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r = M - (N - 1) * 10

ans = []
fans = []

def dfs(i):
    if i == N:
        fans.append(" ".join(map(str, ans)))
        return

    start = max(i * 10 + 1, ans[-1] + 10)
    end = i * 10 + r + 1

    for n in range(start, end):
        ans.append(n)
        dfs(i + 1)
        ans.pop()

for n in range(1, r + 1):
    ans.append(n)
    dfs(1)
    ans.pop()

print(len(fans))
for f in fans:
  print(f)
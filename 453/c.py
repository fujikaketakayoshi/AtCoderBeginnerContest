import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

ans = 0

def dfs(i, pos, cnt):
  global ans
  if i == N:
    ans = max(ans, cnt)
    return
  npos = pos - L[i]
  if (pos > 0 and npos < 0) or (pos < 0 and npos > 0):
    dfs(i + 1, npos, cnt + 1)
  else:
    dfs(i + 1, npos, cnt)
  npos = pos + L[i]
  if (pos > 0 and npos < 0) or (pos < 0 and npos > 0):
    dfs(i + 1, npos, cnt + 1)
  else:
    dfs(i + 1, npos, cnt)
  

dfs(0, 0.5, 0)
print(ans)

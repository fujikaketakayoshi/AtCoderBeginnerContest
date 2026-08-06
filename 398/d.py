import sys
input = sys.stdin.readline
from functools import cache

N, R, C = map(int, input().split())
S = input().strip()
# print(N, R, C, S)

DIR = {
  'N': (-1, 0),
  'S': (1, 0),
  'E': (0, 1),
  'W': (0, -1),
}

@cache
def dfs(s):
  if not s:
    return (0, 0)
  dr, dc = 0, 0
  # print(s, s[-1], s[0:-1])
  dr += DIR[s[-1]][0]
  dc += DIR[s[-1]][1]
  dr2, dc2 = dfs(s[0:-1])
  return (dr + dr2, dc + dc2)

ans = []
for i in range(1, N + 1):
  # print(S[0:i])
  ans.append(1 if (R, C) == dfs(S[0:i]) else 0)

# print(ans)
print(''.join(map(str, ans)))


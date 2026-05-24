import sys
input = sys.stdin.readline

S = input().strip()
# print(S)
n = len(S)

ans = 0
for i, c in enumerate(S):
  # print(i,c)
  if c == 'C':
    num = min(n - 1 - i, i)
    ans += num + 1
print(ans)

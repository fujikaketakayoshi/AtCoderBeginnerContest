import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()
# print(N, S)

one_n = S.count('1')
one_cnt = 0
ans = 0
for i, c in enumerate(S):
  if c == '0':
    ans += min(one_cnt, one_n - one_cnt)
  else:
    one_cnt += 1

print(ans)
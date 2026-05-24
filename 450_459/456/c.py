import sys
input = sys.stdin.readline

MOD = 998244353

S = input().strip()
print(S)

n = len(S)
total = n * (n + 1) // 2
print(total)

prev = ''
succ = 1
cnt = 0
for i, c in enumerate(S):
  if prev == c:
    succ += 1
    print(i, prev, c, succ)
    pre_cnt = i - succ + 1
    post_cnt = n - i - 1
    print('cnt', pre_cnt, post_cnt)
    cnt += post_cnt + pre_cnt + pre_cnt * post_cnt + 1
  else:
    prev = c
    succ = 1

print(total - cnt)
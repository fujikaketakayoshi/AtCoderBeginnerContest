import sys
input = sys.stdin.readline

S = input().strip()

cnt_w = 0
ans = []

for c in S:
    if c == 'W':
        cnt_w += 1
    elif c == 'A' and cnt_w > 0:
        ans.append('A')
        ans.append('C' * cnt_w)
        cnt_w = 0
    else:
        ans.append('W' * cnt_w)
        cnt_w = 0
        ans.append(c)

ans.append('W' * cnt_w)

print(''.join(ans))
import sys
input = sys.stdin.readline

S = input().strip()
# print(S)

a_cnt = 0
b_cnt = 0
c_cnt = 0
for c in S:
  if c == 'A':
    a_cnt += 1
  elif c == 'B' and a_cnt - b_cnt >= 1:
    b_cnt += 1
  elif c == 'C' and b_cnt - c_cnt >= 1:
    c_cnt += 1
  # print(c, a_cnt, b_cnt, c_cnt)
print(c_cnt)
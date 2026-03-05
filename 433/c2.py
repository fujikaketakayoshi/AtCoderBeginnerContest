import sys
input = sys.stdin.readline

S = str(input().strip())

pre = ''
pre_suc = 0
blocks = []

for c in S:
  if pre == '':
    pre = c
    pre_suc += 1
  elif pre == c:
    pre_suc += 1
  elif pre != c:
    blocks.append((pre, pre_suc))
    pre = c
    pre_suc = 1
blocks.append((pre, pre_suc))
# print(blocks)

cnt = 0
i = 1
while i < len(blocks):
  num1, suc1 = blocks[i - 1]
  num2, suc2 = blocks[i]
  if int(num1) + 1 == int(num2):
    cnt += min(suc1, suc2)
  i += 1

print(cnt)
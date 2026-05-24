import sys
input = sys.stdin.readline

T = int(input())

def blocked(S):
  block = []
  succ_cnt = 1
  prev = S[0]
  i = 1
  while i < len(S):
    if S[i] == prev:
      succ_cnt += 1
    else:
      block.append([prev, succ_cnt])
      prev = S[i]
      succ_cnt = 1
    i += 1
  block.append([prev, succ_cnt])
  return block

def del_p(block):
  for i in range(len(block) - 2):
    if block[i + 1] == ['x', 2] and block[i][0] == '(' and block[i][1] > 0 and block[i + 2][0] == ')' and block[i + 2][1] > 0:
      if block[i][1] == block[i + 2][1]:
        del_num = block[i][1]
      else:
        del_num = min(block[i][1], block[i + 2][1])
      block[i][1] -= del_num
      block[i + 2][1] -= del_num
  return block

def rec_s(block):
  tmp = []
  for s, num in block:
    tmp.append(s * num)
  return ''.join(tmp)

for _ in range(T):
  A = input().strip()
  B = input().strip()
  if A.count('x') != B.count('x'):
    print('No')
    continue
  
  ab = blocked(A)
  bb = blocked(B)
  ab = del_p(ab)
  bb = del_p(bb)
  a = rec_s(ab)
  b = rec_s(bb)
  print('Yes' if a == b else 'No')

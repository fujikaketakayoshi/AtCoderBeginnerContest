import sys
input = sys.stdin.readline

N = int(input())
C = []
for _ in range(N):
  Q = input().split()
  if Q[0] == '1':
    if Q[1] == ')':
      if len(C) > 0 and C[-1] == '(':
        C.pop()
      else:
        C.append(Q[1])
    else:
      C.append(Q[1])
  else:
    if len(C) == 0:
      C = ['(']
    else:
      C.pop()
  if len(C) == 0:
    print('Yes')
  else:
    print('No')

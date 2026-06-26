import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

Spc = ''
Sidx = ''
pc = [[] for _ in range(N)]
ss = []
for _ in range(Q):
  query = list(input().split())
  q = int(query[0])
  p = int(query[1]) - 1
  if q == 1:
    pc[p] = pc[Spc][:Sidx] if Spc != '' and Sidx != '' else []
  elif q == 2:
    s = query[2]
    ss.append(s)
    idx = len(ss) - 1
    pc[p].append(idx)
  else:
    n = len(pc[p])
    Spc = p
    Sidx = n
    # print(S)
print(''.join([ss[i] for i in pc[Spc]]) if Spc != '' else '')

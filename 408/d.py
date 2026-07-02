import sys
input = sys.stdin.readline

T = int(input())
T = 1

for _ in range(T):
  N = int(input())
  S = input().strip()
  print(N, S)
  lc = []
  pre = S[0]
  succ = 1
  for i in range(1, N):
    if pre == S[i]:
      succ += 1
    else:
      lc.append((pre, succ))
      pre = S[i]
      succ = 1
  lc.append((pre, succ))
  print(lc)
  longest1 = 0
  longest1idx = None
  for i in range(len(lc)):
    d, s = lc[i]
    if d == '1':
      if longest1 < s:
        longest1 = s
        longest1idx = i
  print(longest1, longest1idx)
  
  for i in range(longest1idx + 1, len(lc) - 1, 2):
    print(i)
    if lc[i][1] > lc[i + 1][1]:
        lc[i + 1] = (lc[i + 1][0], lc[i][1])
    
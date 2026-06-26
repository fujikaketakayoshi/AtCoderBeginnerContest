import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  S = list(map(int, input().split()))
  # print(N, S)
  first = S[0]
  last = S[-1]
  domino = S[1:-1]
  # print(first, domino, last)
  domino.sort()
  newS = [first]
  for d in domino:
    if first < d < last:
      newS.append(d)
  newS.append(last)
  # print(newS)
  
  cnt = 0
  i = 0
  while i < len(newS):
    next = newS[i] * 2
    # preneed = (target // 2) + (target % 2)
    print(newS[i], next)
    stack = []
    j = i + 1
    cand = -1
    while j < len(newS):
      if next >= newS[j] and j == len(newS) - 1:
        cand = j
        cnt += 1
        break
      if next >= newS[j]:
        cand = j
        j += 1
      elif cand != -1:
        cnt += 1
        break
      j += 1
    if cand != -1:
      i = cand
    else:
      i += 1
  print(cnt + 1 if cnt != 0 else -1)
  
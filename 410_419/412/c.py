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
  target = newS.pop()
  while True:
    preneed = (target // 2) + (target % 2)
    # print(target, preneed)
    stack = []
    while newS:
      pre = newS.pop()
      if preneed <= pre and not newS:
        cnt += 1
      elif preneed <= pre:
        stack.append(pre)
      elif stack:
        target = stack.pop()
        newS.append(pre)
        # print(newS)
        cnt += 1
        break
    if not newS:
      break
  print(cnt + 1 if cnt != 0 else -1)
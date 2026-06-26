import sys
input = sys.stdin.readline
import bisect

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
  ok = False
  while i < len(newS):
    next = newS[i] * 2
    idx = bisect.bisect_right(newS, next)
    # print(i, newS[i], idx, newS[idx - 1])
    if idx == len(newS):
      ok = True
      cnt += 1
      break
    elif i == idx - 1:
      break
    elif i <= idx < len(newS):
      i = idx - 1
      cnt += 1
  print(cnt + 1 if ok else -1)

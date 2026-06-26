import sys
input = sys.stdin.readline
from collections import Counter
import bisect

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  # print(N, M)
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  A.sort()
  B.sort(reverse=True)
  cntA = Counter(A)
  setA = set(A)
  # print(cntA, setA, A)
  
  modtotal = 0
  for b in B:
    listA = list(setA)
    modzero = M - b if b % M != 0 else 0
    idx = bisect.bisect_left(listA, modzero)
    # print(idx)
    if idx == len(listA):
      a = listA[0]
    elif listA[idx] == modzero:
      a = listA[idx]
    else:
      if idx + 1 == len(listA):
        a = listA[0]
      else:
        a = listA[idx + 1]
    cntA[a] -= 1
    if cntA[a] == 0:
      setA.remove(a)
    modtotal += (a + b) % M
  print(modtotal)
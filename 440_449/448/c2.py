import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

sortA = []
for i, a in enumerate(A):
  sortA.append((a, i))
sortA.sort()

for _ in range(Q):
  K = int(input())
  tmpA = sortA[:K + 1]
  # print(tmpA)
  B = list(map(int, input().split()))
  for b in B:
    idx = b - 1
    i = 0
    while i < len(tmpA):
      if tmpA[i][1] == idx:
        tmpA.pop(i)
        break
      i += 1
  print(tmpA[0][0])

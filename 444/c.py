import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()
results = set()

if N % 2 == 0:
  pre = 0
  ok = True
  for i in range(N):
    if pre != 0:
      if pre != A[i] + A[-i - 1]:
        ok = False
        break
    pre = A[i] + A[-i - 1]
  if ok:
    results.add(pre)

L = A[-1]
r = -1
for i in range(N - 1, -1, -1):
  if L != A[i]:
    r = i
    break

if r == 0:
  results.add(L)
else:
  ok = True
  for i in range(r + 1):
    if L != A[i] + A[r - i]:
      ok = False
      break
  if ok:
    results.add(L)

print(' '.join(map(str, sorted(results))))

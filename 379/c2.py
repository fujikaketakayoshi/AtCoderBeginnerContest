import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
# print(N, M, X, A)

XA = []
total_s = 0
for i in range(M):
  XA.append((X[i], A[i]))
  total_s += A[i]

if total_s != N:
  print(-1)
  exit()

XA.sort()
# print(XA)

XS = []
s = 0
total_xa = 0
for x, a in XA:
  total_xa += x * a
  s += a
  XS.append((x, s))
# print(N * (N + 1) // 2, total_xa)

if XS[0][0] != 1:
  print(-1)
  exit()

pres = XS[0][1]
for x, s in XS[1:]:
  if x - 1 <= pres:
    pres = s
  else:
    print(-1)
    exit()

print(N * (N + 1) // 2 - total_xa)
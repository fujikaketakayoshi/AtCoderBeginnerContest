import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
# print(N, M, X, A)

XA = []
for i in range(M):
  XA.append((X[i], A[i]))

XA.sort()
# print(XA)

if XA[0][0] != 1:
  print(-1)
  exit()

ans = 0
pos = 1
stone = XA[0][1]
for x, a in XA[1:]:
  k = x - pos
  if k <= stone:
    ans += (k - 1) * k // 2
    ans += k * (stone - k)
    stone -= k
    stone += a
    pos = x
  else:
    print(-1)
    exit()
  

k = N - pos + 1
if k == stone:
  ans += (k - 1) * k // 2
  print(ans)
else:
  print(-1)

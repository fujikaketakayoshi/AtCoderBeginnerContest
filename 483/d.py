import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
print(N, A)

xs = []
x = 0
for a in A:
  x += a
  xs.append(x)

print(xs)
maxs = []
mins = []
ma = float('-inf')
mi = float('inf')
for x in reversed(xs):
  if x < mi:
    mi = x
  if x > ma:
    ma = x
  maxs.append(ma)
  mins.append(mi)
maxs.reverse()
mins.reverse()
print(maxs)
print(mins)
print(ma, mi)

ans = ma - mi
ansmin = 0
ansmax = 0
for i in range(N):
  if xs[i] > 0:
    ansmin = mins[i] - 2 * A[i]
    ans = max(ans, ma - ansmin + 1)
  elif xs[i] < 0:
    ansmax = max(ansmax, xs[i] + 2 * A[i])
    ans = max(ans, ansmax - mi + 1)

print(ans)
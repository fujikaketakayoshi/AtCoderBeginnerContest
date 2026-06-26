import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)
X = list(map(int, input().split()))
X.sort()
# print(X)

dist = []
for i in range(N - 1):
  dist.append(X[i + 1] - X[i])
dist.sort(reverse=True)
# print(dist)

ans = X[-1] - X[0]
for i in range(M - 1):
  ans -= dist[i]
print(ans)

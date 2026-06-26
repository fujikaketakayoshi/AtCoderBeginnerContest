import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)
X = list(map(int, input().split()))
X.sort()
# print(X)

dist = []
for i in range(N - 1):
  dist.append((X[i + 1] - X[i], i))
dist.sort(reverse=True)
# print(dist)

cut_idx = set()
for i in range(M - 1):
  cut_idx.add(dist[i][1])
cut_idx.add(N - 1)
cut = sorted(cut_idx)

ans = 0
prev = 0
for c in cut:
    ans += X[c] - X[prev]
    prev = c + 1
print(ans)

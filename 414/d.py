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
cut_idx.add(-1)
cut_idx.add(N - 1)
cut_idx_sorted = sorted(list(cut_idx))
# print(cut_idx_sorted)

ans = 0
for i in range(len(cut_idx_sorted) - 1):
  idx = cut_idx_sorted[i] + 1
  ra = cut_idx_sorted[i + 1] + 1
  # print(idx, ra)
  # print(X[idx:ra])
  # print(X[idx:ra][-1] - X[idx:ra][0])
  ans += X[idx:ra][-1] - X[idx:ra][0]
print(ans)

import sys
input = sys.stdin.readline

N, D = map(int, input().split())
X = list(map(int, input().split()))
# print(N, D, X)

A = [(-(10**9), 0)]
for i, x in enumerate(X):
  A.append((x, i + 1))
A.append((3 * 10 ** 9, len(X) + 1))

# print(A)
A.sort()

ans = []
for i in range(1, N + 1):
  if A[i][0] - A[i - 1][0] >= D and  A[i + 1][0] - A[i][0] >= D:
    ans.append(A[i][1])

ans.sort()
print(len(ans))
print(*ans)
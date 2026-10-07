import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
# print(N, K, A)

X = sorted(A)
# print(A)

l = 0
for i in range(N):
  # print(i, i + K, A[i], X[i], A[i + K], X[i + K])
  if A[i] == X[i]:
    l += 1
  else:
    break

r = 0
for i in range(N - 1, -1, -1):
  if A[i] == X[i]:
    r += 1
  else:
    break

# print(l, r)
print('Yes' if l + r >= N - K else 'No')

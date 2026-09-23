import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

imos = [0] * (N + 1)
imos_sum = 0
for i, a in enumerate(A):
  imos_sum += imos[i]
  if a + imos_sum > 0:
    imos[i + 1] += 1
    r = i + a + imos_sum
    if r + 1 < N:
      imos[r + 1] -= 1
# print(imos)

imos_sum = 0
ans = []
for i in range(N):
  imos_sum += imos[i]
  v = A[i] + imos_sum - (N - (i + 1))
  v = 0 if v < 0 else v
  ans.append(v)
print(*ans)

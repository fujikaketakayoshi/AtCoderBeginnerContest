import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

sumA = sum(A)

ans = 0
for i in range(N - 1):
  sumA -= A[i]
  ans += A[i] * sumA
print(ans)

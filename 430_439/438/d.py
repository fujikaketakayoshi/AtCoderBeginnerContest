import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
# print(N, A, B, C)

prefA = [0] * (N + 1)
prefB = [0] * (N + 1)
prefC = [0] * (N + 1)
for i in range(1, N + 1):
  prefA[i] = prefA[i - 1] + A[i - 1]
  prefB[i] = prefB[i - 1] + B[i - 1]
  prefC[i] = prefC[i - 1] + C[i - 1]
# print(prefA, prefB, prefC)

ans = 0
for x in range(N):
  for y in range(x + 1, N - 1):
    sumA = prefA[x + 1] - prefA[0]
    sumB = prefB[y + 1] - prefB[x + 1]
    sumC = prefC[-1] - prefC[y + 1]
    ans = max(ans, sumA + sumB + sumC)

print(ans)
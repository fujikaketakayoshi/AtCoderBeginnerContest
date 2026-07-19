import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A, B)
cA = A[:]

cnt0 = 0
if cA[0] == 0:
  1
else:
  cA[0] = 0
  cnt0 += 1
for i in range(N - 1):
  if (cA[i] + cA[i + 1]) % 2 != B[i]:
    cA[i + 1] += 1
    cnt0 += 1

cA = A[:]

cnt1 = 0
if cA[0] == 1:
  1
else:
  cA[0] = 1
  cnt1 += 1
for i in range(N - 1):
  if (cA[i] + cA[i + 1]) % 2 != B[i]:
    cA[i + 1] += 1
    cnt1 += 1

print(min(cnt0, cnt1))
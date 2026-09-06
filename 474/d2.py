import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, A, B)

diff = []
minus = 0
plus = 0
for i in range(N):
  diff.append(A[i] - B[i])
  if A[i] - B[i] <= 0:
    minus += abs(A[i] - B[i])
  else:
    plus += A[i] - B[i]

# print(plus, minus)
if plus == 0:
  print('No')
  exit()

weight = minus // plus + 1
W = []
for d in diff:
  if d <= 0:
    W.append(1)
  else:
    W.append(weight)

print('Yes')
print(*W)

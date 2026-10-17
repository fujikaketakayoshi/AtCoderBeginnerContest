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

# if plus - minus > 0:
#   weight = plus - minus
# elif plus - minus < 0:
#   weight = minus - plus + 2
# else:
#   weight = 2
W = []
for d in diff:
  if d <= 0:
    W.append(1)
  else:
    W.append(10**18)

print('Yes')
print(*W)

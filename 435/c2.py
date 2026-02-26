import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
# print(N, A)

i = 1
reach = 1
while reach <= N:
  # print(i, reach)
  right = i + A[reach]
  for j in range(i, right):
    reach = max(reach, j + A[j] - 1)
  if reach >= N:
    break
  elif A[reach] == 1:
    break
  else:
    i += A[reach] - 1

print(N if reach >= N else reach)

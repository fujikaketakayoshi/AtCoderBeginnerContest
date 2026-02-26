import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
# print(N, A)

i = 1
while i <= N:
  if A[i] == 1:
    break
  else:
    i += A[i] - 1
print(N if i >= N else i)

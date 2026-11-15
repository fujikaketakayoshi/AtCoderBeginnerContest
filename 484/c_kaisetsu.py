import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, A, B)

if A == B:
  print('Yes')
  exit()

l = 0
for i in range(N):
  if A[i] != B[i]:
    l = i
    break
r = 0
for i in range(N - 1, -1, -1):
  if A[i] != B[i]:
    r = i
    break
# print(l, r)
sA = A[l:r + 1]
sB = B[l:r + 1]
# print(sA, sB)

lA = sA[1:] + [sA[0]]
rA = [sA[-1]] + sA[0:-1]
# print(lA, rA)
if lA == sB or rA == sB:
  print('Yes')
else:
  print('No')

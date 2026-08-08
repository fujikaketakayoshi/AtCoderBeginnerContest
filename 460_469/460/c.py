import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
# print(N,M,A,B)

idxa = 0
idxb = 0

cnt = 0
while idxb < len(B):
  if A[idxa] * 2 >= B[idxb]:
    cnt += 1
    idxa += 1
    idxb += 1
  else:
    idxb += 1
  if idxa == len(A):
    break
print(cnt)
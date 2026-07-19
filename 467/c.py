import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(A, B)

nA = [A[0]]
pre = A[0]
for b in B:
  if b == 0:
    if pre == 0:
      nA.append(0)
      pre = 0
    else:
      nA.append(1)
      pre = 1
  else:
    if pre == 0:
      nA.append(1)
      pre = 1
    else:
      nA.append(0)
      pre = 0
# print(nA)
# print(A)
cnt1 = 0
for i in range(N):
  if nA[i] != A[i]:
    cnt1 += 1
    
nA = [A[-1]]
pre = A[-1]
for b in reversed(B):
  if b == 0:
    if pre == 0:
      nA.append(0)
      pre = 0
    else:
      nA.append(1)
      pre = 1
  else:
    if pre == 0:
      nA.append(1)
      pre = 1
    else:
      nA.append(0)
      pre = 0
# print(nA)
# print(A)
nA.reverse()
cnt2 = 0
for i in range(N):
  if nA[i] != A[i]:
    cnt2 += 1


print(cnt1, cnt2)
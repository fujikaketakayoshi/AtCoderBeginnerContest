import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) + [0]
B = list(map(int, input().split())) + [0]
N += 1
# print(N, A, B)


i = 0
ok = True
tmp = None
while i < N and A[i] == B[i]:
  i += 1
  continue

if i == N:
  print('Yes')
  exit()

if A[i] == B[i + 1]:
  tmp = B[i]
  ok = False

while i + 1 < N and A[i] == B[i + 1]:
  i += 1
  continue

if A[i] == tmp:
  ok = True
  i += 1

while i < N and A[i] == B[i]:
  i += 1
  continue

# print(i)

if i == N and ok:
  print('Yes')
  exit()

i = 0
ok = True
tmp = None
while i < N and A[i] == B[i]:
  i += 1
  continue

if A[i + 1] == B[i]:
  tmp = A[i]
  ok = False

while i + 1 < N and A[i + 1] == B[i]:
  i += 1
  continue

if B[i] == tmp:
  ok = True
  i += 1

while i < N and A[i] == B[i]:
  i += 1
  continue

if i == N and ok:
  print('Yes')
else:
  print('No')
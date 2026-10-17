import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(N, M, K)
# print(X, Y)

A.sort()
B.sort()
# print(A, B)

Bans = 0
for b in B:
  knum = (b + K - 1) // K
  onenum = knum * K - b
  if Y - knum < 0:
    break
  Y -= knum
  X += onenum
  Bans += 1
  # print(knum, onenum, X, Y, Bans)

# print(X, Y)
X += Y * K
Aans = 0
for a in A:
  if X - a < 0:
    break
  X -= a
  Aans += 1
  # print(X, Aans)
# print(Aans, Bans)

cont = True
j = Aans
for i in range(Bans - 1, -1, -1):
  X += B[i]
  cont = False
  while j < N:
    if X - A[j] < 0:
      break
    X -= A[j]
    j += 1
    cont = True
  if not cont:
    break
  Bans -= 1
print(j + Bans)
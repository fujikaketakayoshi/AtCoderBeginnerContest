import sys
input = sys.stdin.readline
import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
# print(N, Q, A)

preA = [0] * (N + 1)
for i in range(N):
  preA[i + 1] = preA[i] + A[i]

Bidx = [0]
preB = [0]
for i in range(N):
  Bidx.append(Bidx[i] + (i + 1))
  preB.append(preB[i] + preA[i + 1])
# print(Bidx)
# print(preB)

def f(k):
  idx = bisect.bisect_left(Bidx, k)
  if idx == 0:
    return 0
  # print(idx, preB[idx - 1])
  Aidx = Bidx[idx] - Bidx[idx - 1]
  Adiff = k - Bidx[idx - 1]
  # print('Adiff', Adiff)
  # print(Aidx, Adiff, preA[Adiff])
  return preB[idx - 1] + preA[Adiff]


for _ in range(Q):
  L, R = map(int, input().split())
  # print(L, R)
  print(f(R) - f(L - 1))

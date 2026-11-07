import sys
input = sys.stdin.readline
import bisect

N, S = map(int, input().split())
A = list(map(int, input().split()))
print(N, S, A)
sumA = sum(A)
t = S % sumA
shou = S // sumA
print(sumA, shou, t)
print(shou * sumA + t)

preL = [0] * (N + 1)
for i in range(N):
  preL[i + 1] = preL[i] + A[i]
print(preL)

rA = list(reversed(A))
preR = [0] * (N + 1)
for i in range(N):
  preR[i + 1] = preR[i] + rA[i]
print(preR)

lidx = bisect.bisect_right(preL, t)
while lidx > 0:
  # print(preL[lidx - 1])
  if preL[lidx - 1] == t:
    print('Yes')
    exit()
  diff = t - preL[lidx - 1]
  ridx = bisect.bisect_right(preR, diff)
  print(preL[lidx - 1], diff, preR[ridx - 1])
  if preR[ridx - 1] == diff:
    print('Yes')
    exit()
  lidx -= 1

ridx = bisect.bisect_right(preR, t)
while ridx > 0:
  if preR[ridx - 1] == t:
    print('Yes')
    exit()
  diff = t - preR[ridx - 1]
  lidx = bisect.bisect_right(preL, diff)
  print(preR[ridx - 1], diff, preL[lidx - 1])
  if preL[lidx - 1] == diff:
    print('Yes')
    exit()
  ridx -= 1



print('No')
import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
print(N, P, Q)



i = 0
top = 0
while i < N:
  if P[i] == Q[i]:
    i += 1
    continue
  elif P[i] > Q[i]:
    print(0)
    exit()
  else:
    top = i
    break

ans = 0
Pused = set()
Qused = set()

Pbai = 1
Qbai = 1
for i, p in enumerate(P):
  if i < top:
    Pused.add(P[i])
    Qused.add(Q[i])
    continue
  elif i == top:
    Pbai = Q[i] - P[i]
    Pused.add(P[i])
    Qused.add(Q[i])
  else:
    cnt = N - P[i] + 1
    for p in range(P[i], N + 1):
      if p in Pused:
        cnt -= 1
    if cnt > 0:
      Pbai *= cnt
    Pused.add(P[i])
    
    cnt = Q[i]
    for q in range(1, Q[i] + 1):
      if q in Qused:
        cnt -= 1
    if cnt > 0:
      Qbai *= cnt
    Qused.add(Q[i])

print(Pbai, Qbai)
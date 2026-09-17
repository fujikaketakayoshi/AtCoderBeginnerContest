import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

PH = [0] * (N + 1)
Hnum = [0] + [1] * N
for i in range(1, N + 1):
  PH[i] = i
# print(PH, Hnum)

ans = 0
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    P, H = query[1:]
    before = PH[P]
    Hnum[before] -= 1
    if Hnum[before] == 1:
      ans -= 1
    PH[P] = H
    Hnum[H] += 1
    if Hnum[H] == 2:
      ans += 1
  else:
    print(ans)
    # print('2!')

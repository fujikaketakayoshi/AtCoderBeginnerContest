import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)
INF = 10 ** 20

L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]
# print(L)
# print(R)

Lmin = L[:]
for i in range(N - 2, -1, -1):
  Lmin[i] = min(Lmin[i], Lmin[i + 1])

Rmin = R[:]
for i in range(1, N):
  Rmin[i] = min(Rmin[i], Rmin[i - 1])
# print(Lmin)
# print(Rmin)

for _ in range(Q):
  s, t = map(int, input().split())
  # print(s, t)
  s -= 1
  t -= 1
  ans = float('inf')
  if s < t:
    # 右に即移動
    ans = min(ans, R[s])
    # 左に行って右へ
    ans = min(ans, L[s] + Rmin[s])
  else:
    # 左に即移動
    ans = min(ans, L[s])
    # 右に行って左へ
    ans = min(ans, R[s] + Lmin[s])
  print(ans)

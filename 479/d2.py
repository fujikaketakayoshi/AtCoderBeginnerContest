import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)
INF = 10 ** 20

L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]
# print(L)
# print(R)

Lmini = [0] * N
lmini = 0
lmin = float('inf')
for i in range(N - 1, -1, -1):
  if L[i] < lmin:
    lmin = L[i]
    lmini = i
  Lmini[i] = lmini

Rmini = [N - 1] * N
rmini = N - 1
rmin = float('inf')
for i in range(N):
  if R[i] < rmin:
    rmin = R[i]
    rmini = i
  Rmini[i] = rmini

# print(Lmini)
# print(Rmini)

for _ in range(Q):
  s, t = map(int, input().split())
  # print(s, t)
  s -= 1
  t -= 1
  ans = float('inf')
  if s < t:
    # print(R[s], L[s], Rmini[s], R[Rmini[s]])
    # 右に即移動
    ans = min(ans, R[s])
    # 左に行って右へ
    ans = min(ans, L[s] + R[Rmini[s]])
  else:
    # print(L[s], R[s], Lmini[s], L[Lmini[s]])
    # 左に即移動
    ans = min(ans, L[s])
    # 右に行って左へ
    ans = min(ans, R[s] + L[Lmini[s]])
  print(ans)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
# print(N, K, A)

cnt = [0] * (N + 1)

wmin = 10 ** 30
wmax = 0
for i in range(K):
  cnt[A[i]] += 1
  wmin = min(wmin, A[i])
  wmax = max(wmax, A[i])
# print(wmin, wmax)

Amm = [(wmin, wmax)]

# print(Amm)

for i in range(K, N):
  # print(i, i - K, A[i], A[i - K])
  cnt[A[i]] += 1
  wmin = min(wmin, A[i])
  wmax = max(wmax, A[i])
  cnt[A[i - K]] -= 1
  if A[i - K] == wmin and cnt[A[i - K]] == 0:
    v = A[i - K] + 1
    while v < N + 1:
      if cnt[v] > 0:
        wmin = v
        break
      v += 1
  if A[i - K] == wmax and cnt[A[i - K]] == 0:
    v = A[i - K] - 1
    while v > 0:
      if cnt[v] > 0:
        wmax = v
        break
      v -= 1
  
  Amm.append((wmin, wmax))
# print(Amm)

A = [0] + A[:] + [10 ** 30]
window_l = set()
for i in range(K + 1, N + 1):
  if A[i - K - 1] <= A[i - K]:
    window_l.add(i - K - 1)
  else:
    break
# print(i - K, i, A[i - K], A[i])
# print(window_l)

window_r = set()
for i in range(N, K, -1):
  # print(A[i], A[i + 1])
  if A[i] <= A[i + 1]:
    window_r.add(i - 1)
  else:
    break
# print(window_r)

for i in range(N - K):
  # print(i, K + i, A[i], A[K + i + 1], A[i] <= Amm[i][0], Amm[i][1] <= A[K + i + 1])
  if i in window_l and K + i in window_r and A[i] <= Amm[i][0] and Amm[i][1] <= A[K + i + 1]:
  # if A[i] <= Amm[i][0] and Amm[i][1] <= A[K + i + 1]:
    print('Yes')
    exit()
print('No')
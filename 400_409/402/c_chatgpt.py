import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

remain = [0] * M
foods = [[] for _ in range(N + 1)]
for m in range(M):
  q = list(map(int, input().split()))
  K = q[0]
  remain[m] = K
  A = q[1:]
  for a in A:
    foods[a].append(m)

B = list(map(int, input().split()))
# print(B)

ans = 0
for b in B:
  for m in foods[b]:
    remain[m] -= 1
    if remain[m] == 0:
      ans += 1
  print(ans)

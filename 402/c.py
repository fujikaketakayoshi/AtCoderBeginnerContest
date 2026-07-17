import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)

Ks = [set() for _ in range(M + 1)]
cnt = [set() for _ in range(N + 1)]
for m in range(1, M + 1):
  q = list(map(int, input().split()))
  K = q[0]
  A = q[1:]
  for a in A:
    Ks[m].add(a)
    cnt[a].add(m)
  # print(K, A)
# print(Ks)

B = list(map(int, input().split()))
# print(B)

ans = 0
for b in B:
  for m in cnt[b]:
    Ks[m].remove(b)
    if len(Ks[m]) == 0:
      ans += 1
  print(ans)
      
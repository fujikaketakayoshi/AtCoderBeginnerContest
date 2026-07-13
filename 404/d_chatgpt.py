import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)
C = list(map(int, input().split()))
# print(C)

N_ani = [[] for _ in range(N + 1)]
As = [[]]
for m in range(1, M + 1):
  KA = list(map(int, input().split()))
  K = KA[0]
  A = KA[1:]
  for a in A:
    N_ani[a].append(m)

# print(N_ani)

ans = float('INF')
n3max = 3 ** N
for n in range(n3max):
  x = n
  cost = 0
  cnt = [0] * (M + 1)
  done = [False] * (M + 1)
  remain = M
  for i in range(N):
    v = x % 3
    x //= 3
    if v > 0:
      for k in N_ani[i + 1]:
        cnt[k] += v
        if cnt[k] >= 2 and not done[k]:
          done[k] = True
          remain -= 1
      cost += C[i] * v
  if remain == 0:
    ans = min(ans, cost)
  # print(s3, cost)
print(ans)
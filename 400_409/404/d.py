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

def base_n(num, base):
    if num == 0:
        return "0"

    s = ""
    while num:
        s = str(num % base) + s
        num //= base

    return s

ans = float('INF')
n3max = 3 ** N
for n in range(n3max):
  s3 = base_n(n, 3).zfill(N)
  cost = 0
  cnt = [0] * (M + 1)
  yet2seen = set(map(int, range(1, M + 1)))
  for i, v in enumerate(s3):
    v = int(v)
    if v > 0:
      for k in N_ani[i + 1]:
        cnt[k] += v
        if cnt[k] >= 2 and k in yet2seen:
          yet2seen.remove(k)
      cost += C[i] * v
  if not yet2seen:
    ans = min(ans, cost)
  # print(s3, cost)
print(ans)
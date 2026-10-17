import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
P = list(map(int, input().split()))
# print(N, Q, P)

pos = [0] * (N + 1)

for i, p in enumerate(P):
    pos[p] = i

last = N
for _ in range(Q):
    a = int(input())
    pos[a] = last
    last += 1

tmp = [0] * (N + Q + 1)
for v, idx in enumerate(pos):
  tmp[idx] = v

ans = []
for v in tmp:
  if v == 0:
    continue
  ans.append(v)


print(*ans)
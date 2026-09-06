import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
P = list(map(int, input().split()))
# print(N, Q, P)

idx = [0] * (N + 1)
for i, p in enumerate(P):
  idx[p] = i
# print(idx)

last = N
for _ in range(Q):
  a = int(input())
  # print(a)
  idx[a] = last
  last += 1

# print(idx)
sorted_idx = sorted(idx, key=idx.get)
# print(sorted_idx)
ans = []
for v in sorted_idx:
  ans.append(v)

print(*ans)
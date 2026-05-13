import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
# print(N, Q, A)
# print(pre_sum)

AW = A * 2
# print(AW)
pre_sum = [0] * (2 * N + 1)
for i, a in enumerate(AW):
  pre_sum[i + 1] = pre_sum[i] + a

start = 0
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    c = query[1]
    start = (start + c) % N
  else:
    l, r = query[1], query[2]
    print(pre_sum[r + start] - pre_sum[l - 1 + start])

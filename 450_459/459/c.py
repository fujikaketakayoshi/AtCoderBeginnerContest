import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

MAX = 3 * 10 ** 5 * 2 + 1
blocks = [0] * N
size_index = [[] for _ in range(MAX)]
size_index[0] = list(range(N))
# print(size_index)
size_cnt = 1
for _ in range(Q):
  q, xy = map(int, input().split())
  # print(q, xy)
  if q == 1:
    x = xy
    x -= 1
    blocks[x] += 1
    size_index[blocks[x]].append(x)
    if len(size_index[size_cnt]) == N:
      size_cnt += 1
  elif q == 2:
    y = xy
    limit_size = size_cnt - 1 + y
    print(len(size_index[limit_size]))

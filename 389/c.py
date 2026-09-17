import sys
input = sys.stdin.readline

Q = int(input())
# print(Q)

q = []
head_l = 0
ex_l = 0
head_idx = 0
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    l = query[1]
    q.append((head_l, l))
    head_l += l
  elif query[0] == 2:
    m = q[head_idx][1]
    ex_l += m
    head_idx += 1
  else:
    k = query[1]
    # print(q, head_idx, k)
    print(q[head_idx + k - 1][0] - ex_l)
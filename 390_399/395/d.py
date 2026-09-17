import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

p_idx = []
for i in range(N + 1):
  p_idx.append(i)
# print(p_idx)

n_ps = [set([i]) for i in range(N + 1)]
# print(n_ps)

for _ in range(Q):
  query = list(map(int, input().split()))
  # print(query)
  if query[0] == 1:
    a, b = query[1:3]
    n_ps[p_idx[a]].remove(a)
    n_ps[b].add(a)
    p_idx[a] = b
  elif query[0] == 2:
    a, b = query[1:3]
    for p in n_ps[a]:
      p_idx[p] = b
    for p in n_ps[b]:
      p_idx[p] = a
    n_ps[a], n_ps[b] = n_ps[b], n_ps[a]
  else:
    a = query[1]
    # print(p_idx)
    print(p_idx[a])

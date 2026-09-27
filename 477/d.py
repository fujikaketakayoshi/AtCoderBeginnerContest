import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

queries = []
for _ in range(Q):
  query = input().split()
  if query[0] == '1':
    X = int(query[1])
    queries.append((1, X))
  else:
    C = query[1]
    queries.append((2, C))
# print(queries)

q2cnt = 0
queries2 = []
for q, xc in reversed(queries):
  if q2cnt > 0 and q == 1:
    queries2.append((q, xc))
  elif q == 2:
    q2cnt += 1
    queries2.append((q, xc))
# print(queries2)

masked = [False] * (N + 1)
for q, xc in reversed(queries2):
  if q == 1:
    masked[xc] = not masked[xc]
# print(masked)


masked_false = set()
masked_true = set()
for i, tf in enumerate(masked):
  if not tf:
    masked_false.add(i)
  else:
    masked_true.add(i)

ans = ['a'] * (N + 1)
for q, xc in queries2:
  if q == 1:
    if xc in masked_false:
      masked_false.remove(xc)
      masked_true.add(xc)
    elif xc in masked_true:
      masked_true.remove(xc)
      masked_false.add(xc)
  elif q == 2:
    for i in masked_false:
      ans[i] = xc
    masked_false = set()

print(''.join(ans[1:]))
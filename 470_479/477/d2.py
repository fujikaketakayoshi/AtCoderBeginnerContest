import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# print(N, Q)

masked = [False] * (N + 1)
queries = []
for _ in range(Q):
  query = input().split()
  if query[0] == '1':
    X = int(query[1])
    masked[X] = not masked[X]
    queries.append((1, X))
  else:
    C = query[1]
    queries.append((2, C))
# print(queries)

masked_false = set()
masked_true = set()
for i, tf in enumerate(masked):
  if not tf:
    masked_false.add(i)
  else:
    masked_true.add(i)

ans = ['a'] * (N + 1)
for q, xc in reversed(queries):
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
    masked_false.clear()

print(''.join(ans[1:]))
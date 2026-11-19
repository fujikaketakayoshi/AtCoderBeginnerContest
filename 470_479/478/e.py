import sys
input = sys.stdin.readline
from collections import defaultdict
from collections import deque

N, Q = map(int, input().split())
# print(N, Q)

t0g = defaultdict(list)
t0rg = defaultdict(list)
t1g = defaultdict(list)
t1rg = defaultdict(list)
for _ in range(Q):
  t, u, v = map(int, input().split())
  # print(t,u,v)
  u -= 1
  v -= 1
  if t == 0:
    t0g[u].append(v)
    t0rg[v].append(u)
  elif t == 1 and u == v:
    print('No')
    exit()
  else:
    t1g[u].append(v)
    t1rg[v].append(u)

# print(t0g)
# print(t0rg)
# print(t1g)
# print(t1rg)

ans = [1] * N

if len(t1g.keys()) == 0:
  print('Yes')
  print(*ans)
  exit()
start = list(t1g.keys())[0]

q = deque()
q.append(start)
visited = [False] * N
visited[start] = True
last_u = start
while q:
  u = q.popleft()
  last_u = u
  for v in t1g[u]:
    if visited[v]:
      continue
    q.append(v)
    visited[v] = True
    ans[v] = ans[u] + 1
# print(last_u, ans)

q = deque()
q.append(last_u)
visited = [False] * N
visited[last_u] = True
while q:
  u = q.popleft()
  for v in t1rg[u]:
    if visited[v]:
      continue
    if ans[v] <= ans[u]:
      ans[v] = ans[u] - 1
    q.append(v)
    visited[v] = True
# print(ans)

if len(t0g.keys()) == 0:
  print('Yes')
  print(*ans)
  exit()
start0 = list(t0g.keys())[0]
q = deque()
q.append(start0)
visited = [False] * N
visited[start0] = True
last_u = start0
while q:
  u = q.popleft()
  last_u = u
  for v in t0g[u]:
    if visited[v]:
      continue
    if ans[u] <= ans[v]:
      1
    else:
      print('No')
      exit()
    q.append(v)
    visited[v] = True
# print(last_u)

q = deque()
q.append(last_u)
visited = [False] * N
visited[last_u] = True
while q:
  u = q.popleft()
  for v in t0rg[u]:
    if visited[v]:
      continue
    if ans[v] <= ans[u]:
      1
    else:
      print('No')
      exit()
    q.append(v)
    visited[v] = True

amin = min(ans)
amax = max(ans)
diff = None
if amin <= 0:
  diff = abs(amin) + 1
elif amax > N:
  diff = N - amax

if diff is not None:
  for i in range(N):
    ans[i] += diff
print('Yes')
print(*ans)

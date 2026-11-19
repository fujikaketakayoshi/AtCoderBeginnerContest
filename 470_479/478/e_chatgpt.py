import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

g = [[] for _ in range(N)]
rg = [[] for _ in range(N)]
edges = []

for _ in range(Q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1

    g[u].append(v)
    rg[v].append(u)
    edges.append((t, u, v))

# 1. 順グラフでDFSして帰りがけ順を求める
visited = [False] * N
order = []

for i in range(N):
  stack = [(i, False)]

  while stack:
    u, finished = stack.pop()

    if finished:
        order.append(u)
        continue

    if visited[u]:
        continue

    visited[u] = True
    stack.append((u, True))

    for v in g[u]:
        if not visited[v]:
            stack.append((v, False))
print(order)

# 2. 逆グラフで強連結成分(SCC)を求める
comp = [-1] * N
cid = 0

for i in reversed(order):
    if comp[i] != -1:
        continue

    stack = [i]
    comp[i] = cid

    while stack:
        u = stack.pop()

        for v in rg[u]:
            if comp[v] == -1:
                comp[v] = cid
                stack.append(v)

    cid += 1
print(comp)

# 3. 強連結成分内部の矛盾をチェック
for t, u, v in edges:
    if t == 1 and comp[u] == comp[v]:
        print('No')
        exit()

# 4. 強連結成分番号をそのまま利用
ans = [c + 1 for c in comp]

print('Yes')
print(*ans)
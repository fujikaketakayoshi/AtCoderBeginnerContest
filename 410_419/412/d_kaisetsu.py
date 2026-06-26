import itertools
N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    G[u][v] = G[v][u] = 1
edges = [(i, j) for i in range(N) for j in range(i + 1, N)]
ans = 1 << 30
for e in itertools.combinations(edges, N):
    deg = [0] * N
    for u, v in e:
        deg[u] += 1
        deg[v] += 1
    if all(d == 2 for d in deg):
        ans = min(ans, N + M - 2 * sum(G[u][v] for u, v in e))
print(ans)

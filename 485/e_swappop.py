import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
edges = []

for m in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1

    edges.append((v, c))
    graph[u].append(m)

q = deque([(0, 0, -1)])

while q:
    u, cnt, prec = q.popleft()

    if u == N - 1:
        print(cnt)
        exit()

    i = 0

    while i < len(graph[u]):
        m = graph[u][i]
        v, c = edges[m]

        if c == prec:
            i += 1
            continue

        q.append((v, cnt + 1, c))

        # swap and pop
        last_m = graph[u][-1]
        graph[u][i] = last_m
        graph[u].pop()

        # iは進めない
        # 末尾から移動した辺を次に調べる

print(-1)
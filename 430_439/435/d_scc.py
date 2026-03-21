import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
rgraph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    # x -= 1
    # y -= 1
    graph[x].append(y)
    rgraph[y].append(x)

# ---------- 1. SCC (Kosaraju) ----------

visited = [False] * (N + 1)
order = []

def dfs(v):
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)
    order.append(v)

for v in range(N + 1):
    if not visited[v]:
        dfs(v)

print(order)

scc_id = [-1] * (N + 1) 
scc_count = 0

def rdfs(v):
    scc_id[v] = scc_count
    for nv in rgraph[v]:
        if scc_id[nv] == -1:
            rdfs(nv)

for v in reversed(order):
    if scc_id[v] == -1:
        rdfs(v)
        scc_count += 1
print(scc_id)

# ---------- 2. SCC-DAG 作成 ----------

rdag = [[] for _ in range(scc_count)]

for v in range(N + 1):
    for nv in graph[v]:
        if scc_id[v] != scc_id[nv]:
            rdag[scc_id[nv]].append(scc_id[v])

# ---------- 3. クエリ処理 ----------

Q = int(input())
can = [False] * scc_count  # そのSCCから黒へ到達可能か

def propagate(start):
    q = deque([start])
    can[start] = True
    while q:
        v = q.popleft()
        for nv in rdag[v]:
            if not can[nv]:
                can[nv] = True
                q.append(nv)

for _ in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1:
        # v = tmp[1] - 1
        v = tmp[1]
        sid = scc_id[v]
        if not can[sid]:
            propagate(sid)
    else:
        # v = tmp[1] - 1
        v = tmp[1]
        if can[scc_id[v]]:
            print("Yes")
        else:
            print("No")

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [[] for _ in range(N)]
for i in range(1, N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, i))
    graph[b].append((a, i))

print(graph)

# 頂点0を根にして、親と「親につながる辺の番号」を記録
parent = [-1] * N
edge_id = [0] * N

# キューでのBFS
q = deque()
q.append(0)
order = []
while q:
    v = q.popleft()
    order.append(v)
    for nv, i in graph[v]:
        if nv == parent[v]:
            continue
        parent[nv] = v
        edge_id[nv] = i
        q.append(nv)

print(parent)
print(edge_id)
print(order)

# 子から親へ、部分木の人数を集計
size = [1] * N

for v in reversed(order):
    if parent[v] != -1:
        size[parent[v]] += size[v]

print(size)

# 全員に足す値
base = 0

# 各部分木の入口に記録する加減算
add = [0] * N

for v in order:
    if parent[v] == -1:
        continue

    i = edge_id[v]

    if size[v] > N // 2:
        # 子側が多数：子側の部分木全体に +i
        add[v] += i
    else:
        # 親側が多数：全員に +i、子側の部分木全体に -i
        base += i
        add[v] -= i

print(base, add)
# 親から子へ伝えて、部分木への加減算を反映
for v in order:
    if parent[v] != -1:
        add[v] += add[parent[v]]

print(add)

ans = [base + add[v] for v in range(N)]
print(*ans)
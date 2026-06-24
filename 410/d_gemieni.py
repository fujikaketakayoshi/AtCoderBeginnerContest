import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

adj = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))

# 隣接リストの構築 (1-indexedを0-indexedに変換)

# visited[v][w]: 頂点 v に XOR和 w で到達可能か
# 重みの最大値が 1023 なので、XOR和の範囲は 0 から 1023
MAX_XOR = 1024
visited = [[False] * MAX_XOR for _ in range(N)]

# 初期状態：頂点 0 (元の頂点1) に XOR和 0 で到達
queue = deque([(0, 0)])
visited[0][0] = True

# BFSによる探索
while queue:
    u, curr_xor = queue.popleft()

    for v, w in adj[u]:
        next_xor = curr_xor ^ w
        if not visited[v][next_xor]:
            visited[v][next_xor] = True
            queue.append((v, next_xor))

# 頂点 N-1 (元の頂点N) に到達可能な XOR和のうち、最小のものを探す
ans = -1
for w in range(MAX_XOR):
    if visited[N - 1][w]:
        ans = w
        break

print(ans)

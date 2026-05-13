import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u - 1, v - 1))

ans = M

for mask in range(1 << N):
    remove = 0

    for u, v in edges:
        color_u = (mask >> u) & 1
        color_v = (mask >> v) & 1

        if color_u == color_v:
            remove += 1

    ans = min(ans, remove)

print(ans)
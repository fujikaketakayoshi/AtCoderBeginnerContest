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
    bit = bin(mask)[2:].zfill(N)

    for u, v in edges:
        color_u = bit[N - u - 1]
        color_v = bit[N - v - 1]
        print(color_u, color_v)

        if color_u == color_v:
            remove += 1
    print(remove)
    ans = min(ans, remove)

print(ans)
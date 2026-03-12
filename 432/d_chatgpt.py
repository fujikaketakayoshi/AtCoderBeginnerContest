import sys
input = sys.stdin.readline

N, X, Y = map(int, input().split())

C = []
A = []
B = []

for _ in range(N):
    c, a, b = input().split()
    C.append(c)
    A.append(int(a))
    B.append(int(b))

# 分割境界
INF = 10**18
xs = [-INF, INF]
ys = [-INF, INF]

for i in range(N):
    if C[i] == "X":
        xs.append(A[i])
    else:
        ys.append(A[i])

xs = sorted(set(xs))
ys = sorted(set(ys))

nx = len(xs) - 1
ny = len(ys) - 1

# UnionFind
parent = list(range(nx * ny))
size = [0] * (nx * ny)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        parent[rb] = ra
        size[ra] += size[rb]

# セルが黒か判定
black = [[False]*ny for _ in range(nx)]

for i in range(nx):
    for j in range(ny):
        xl, xr = xs[i], xs[i+1]
        yl, yr = ys[j], ys[j+1]

        if xr - xl <= 0 or yr - yl <= 0:
            continue

        x = (xl + xr) // 2
        y = (yl + yr) // 2

        # 逆操作
        for k in reversed(range(N)):
            if C[k] == "X":
                if x < A[k]:
                    y -= B[k]
                else:
                    y += B[k]
            else:
                if y < A[k]:
                    x -= B[k]
                else:
                    x += B[k]

        if 0 <= x < X and 0 <= y < Y:
            black[i][j] = True
            idx = i*ny + j
            size[idx] = (xr-xl)*(yr-yl)

# Union
for i in range(nx):
    for j in range(ny):
        if not black[i][j]:
            continue

        id1 = i*ny + j

        if i+1 < nx and black[i+1][j]:
            union(id1, (i+1)*ny + j)

        if j+1 < ny and black[i][j+1]:
            union(id1, i*ny + (j+1))

# 面積集計
res = {}
for i in range(nx):
    for j in range(ny):
        if not black[i][j]:
            continue
        idx = i*ny + j
        r = find(idx)
        res.setdefault(r, 0)
        res[r] += size[idx]

ans = sorted(res.values())

print(len(ans))
print(*ans)
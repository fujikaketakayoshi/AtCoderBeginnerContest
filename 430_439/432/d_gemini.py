import sys

# 再帰上限を増やす（Union-Find用）
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    N = int(input_data[0])
    X_limit = int(input_data[1])
    Y_limit = int(input_data[2])
    
    # intervals: (現在のL, 現在のR, 相手の軸への累積移動量)
    # 初期状態は元の黒マス範囲 [0, X_limit), [0, Y_limit)
    xs = [(0, X_limit, 0)]
    ys = [(0, Y_limit, 0)]

    idx = 3
    for _ in range(N):
        C = input_data[idx]
        A = int(input_data[idx+1])
        B = int(input_data[idx+2])
        idx += 3
        
        new_intervals = []
        if C == 'X':
            # xの場所によってyがシフトする
            for L, R, shift_y in xs:
                if R <= A:
                    new_intervals.append((L, A if False else R, shift_y + B))
                elif L >= A:
                    new_intervals.append((L, R, shift_y - B))
                else:
                    new_intervals.append((L, A, shift_y + B))
                    new_intervals.append((A, R, shift_y - B))
            xs = new_intervals
        else:
            # yの場所によってxがシフトする
            for L, R, shift_x in ys:
                if R <= A:
                    new_intervals.append((L, R, shift_x + B))
                elif L >= A:
                    new_intervals.append((L, R, shift_x - B))
                else:
                    new_intervals.append((L, A, shift_x + B))
                    new_intervals.append((A, R, shift_x - B))
            ys = new_intervals

    # 最終的な各区間の「実体」を整理
    # xs, ys は (最終的な座標範囲L, R, 相手の軸へのズレ量) になっている
    # このペア (x_interval, y_interval) が 1 つの「矩形」を形成する
    
    # 連結判定のために、x区間とy区間のインデックスで管理
    NX = len(xs)
    NY = len(ys)
    
    # 隣接リストを作成してBFS/DFSで連結成分を求める
    # 矩形 (i, j) が (i', j') と隣接する条件:
    # 1. i == i' かつ (jとj'がy軸で隣接しており、かつその時のxへの影響shift_xが同じ)
    # 2. j == j' かつ (iとi'がx軸で隣接しており、かつその時のyへの影響shift_yが同じ)

    # 1. x軸方向の隣接関係を整理
    xs.sort()
    x_adj = []
    for i in range(NX - 1):
        if xs[i][1] == xs[i+1][0] and xs[i][2] == xs[i+1][2]:
            x_adj.append((i, i+1))
            
    # 2. y軸方向の隣接関係を整理
    ys.sort()
    y_adj = []
    for j in range(NY - 1):
        if ys[j][1] == ys[j+1][0] and ys[j][2] == ys[j+1][2]:
            y_adj.append((j, j+1))

    # Union-Findで連結成分をまとめる
    parent = list(range(NX * NY))
    def find(a):
        if parent[a] == a: return a
        parent[a] = find(parent[a])
        return parent[a]
    
    def unite(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_a] = root_b

    # xが隣接している組 (i, i+1) について、全てのjで (i,j) と (i+1,j) を繋ぐ
    for i, ni in x_adj:
        for j in range(NY):
            unite(i * NY + j, ni * NY + j)
            
    # yが隣接している組 (j, j+1) について、全てのiで (i,j) と (i,j+1) を繋ぐ
    for j, nj in y_adj:
        for i in range(NX):
            unite(i * NY + j, i * NY + nj)

    # 各連結成分の面積を集計
    areas = {}
    for i in range(NX):
        w = xs[i][1] - xs[i][0]
        for j in range(NY):
            h = ys[j][1] - ys[j][0]
            root = find(i * NY + j)
            areas[root] = areas.get(root, 0) + w * h
            
    ans = sorted(areas.values())
    print(len(ans))
    print(*(ans))

solve()
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N, X, Y = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
    idx += 3
    
    storms = []
    for _ in range(N):
        C = input_data[idx]
        A = int(input_data[idx+1])
        B = int(input_data[idx+2])
        idx += 3
        storms.append((C, A, B))
    
    # 問題文の変換を正確に解釈:
    # after[x,y] = before[x, y+B] (C=X, x<A)  => マスは y方向に -B シフト
    # after[x,y] = before[x, y-B] (C=X, x>=A) => マスは y方向に +B シフト
    # after[x,y] = before[x+B, y] (C=Y, y<A)  => マスは x方向に -B シフト
    # after[x,y] = before[x-B, y] (C=Y, y>=A) => マスは x方向に +B シフト
    #
    # 矩形 (x1,x2,y1,y2) を管理し、各嵐で分割・移動する。
    # N<=14 なので最大 2^14=16384 個の矩形が生じる。
    
    rects = [(0, X-1, 0, Y-1)]
    
    for C, A, B in storms:
        new_rects = []
        for (x1, x2, y1, y2) in rects:
            if C == 'X':
                # x<A の部分: y -= B
                if x1 <= A-1:
                    rx2 = min(x2, A-1)
                    new_rects.append((x1, rx2, y1-B, y2-B))
                # x>=A の部分: y += B
                if x2 >= A:
                    rx1 = max(x1, A)
                    new_rects.append((rx1, x2, y1+B, y2+B))
            else:  # C == 'Y'
                # y<A の部分: x -= B
                if y1 <= A-1:
                    ry2 = min(y2, A-1)
                    new_rects.append((x1-B, x2-B, y1, ry2))
                # y>=A の部分: x += B
                if y2 >= A:
                    ry1 = max(y1, A)
                    new_rects.append((x1+B, x2+B, ry1, y2))
        rects = new_rects
    
    # 2つの矩形が隣接しているかチェック (マスレベルで辺を共有)
    # 条件: (x方向で隣接 かつ y方向で重複) または (y方向で隣接 かつ x方向で重複)
    def rects_adjacent(r1, r2):
        x1a, x2a, y1a, y2a = r1
        x1b, x2b, y1b, y2b = r2
        x_ov  = max(x1a, x1b) <= min(x2a, x2b)
        y_ov  = max(y1a, y1b) <= min(y2a, y2b)
        x_adj = (min(x2a, x2b) + 1 == max(x1a, x1b))
        y_adj = (min(y2a, y2b) + 1 == max(y1a, y1b))
        return (x_adj and y_ov) or (y_adj and x_ov)
    
    # Union-Find で連結成分を求める
    n = len(rects)
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    
    for i in range(n):
        for j in range(i+1, n):
            if rects_adjacent(rects[i], rects[j]):
                union(i, j)
    
    # 各連結成分のマス数を集計
    comp_sizes = defaultdict(int)
    for i, (x1, x2, y1, y2) in enumerate(rects):
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        comp_sizes[find(i)] += area
    
    sizes = sorted(comp_sizes.values())
    print(len(sizes))
    print(*sizes)

solve()
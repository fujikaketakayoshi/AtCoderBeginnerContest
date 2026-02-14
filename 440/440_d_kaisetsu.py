import sys
from bisect import bisect_left

def solve():
    # 入力を一度に読み込んで高速化
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    # リスト A をソート
    A = sorted(map(int, input_data[2:2+N]))
    
    # 各クエリの処理
    results = []
    ptr = 2 + N
    for _ in range(Q):
        X = int(input_data[ptr])
        Y = int(input_data[ptr+1])
        ptr += 2
        
        # 1. X 以上の A の要素が始まるインデックス si を探す
        # si は a[si] >= X となる最小のインデックス
        si = bisect_left(A, X)
        
        # 2. ti を二分探索する
        # 「X 以上 A[ti] 以下の欠番の数」が Y 以上になる最小の ti を探す
        # 条件式: (A[ti] - X + 1) - (ti - si + 1) >= Y
        
        ok = N  # a[n] = +∞ とみなす番兵
        ng = si - 1
        
        while ng + 1 < ok:
            mid = (ok + ng) // 2
            # X 以上 A[mid] 以下の整数の個数: A[mid] - X + 1
            # そのうち A に含まれる個数: mid - si + 1
            # 欠番の数 = (全体) - (含まれる数)
            missing_count = (A[mid] - X + 1) - (mid - si + 1)
            
            if missing_count >= Y:
                ok = mid
            else:
                ng = mid
        
        # 3. 答えの計算
        # X 以上で、A の要素をいくつ飛び越える必要があるか？
        # 最終的に ok インデックスの直前までにある A の要素の数は (ok - si) 個
        # 本来の Y 番目 (X + Y - 1) に、その「飛び越えた A の個数」を足す
        ans = X + (Y - 1) + (ok - si)
        results.append(str(ans))
    
    # 最後にまとめて出力
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
import sys
import bisect
input = sys.stdin.readline

# 高速な入力読み込み
N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# クエリ処理用のデータ
queries = []
for _ in range(Q):
    X, Y = map(int, input().split())
    queries.append((X, Y))

# v 以下の数の中で A に含まれないものの個数を返す関数
def count_not_in_A(v):
    idx = bisect.bisect_right(A, v)
    return v - idx

results = []
for X, Y in queries:
    # X-1 までに「欠番」がいくつあるか
    base_count = count_not_in_A(X - 1)
    target = base_count + Y
    
    # 答えとなる値を二分探索で探す
    low = X
    high = 2 * 10**9 # X_max + Y_max 程度の十分大きな値
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if count_not_in_A(mid) >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    results.append(str(ans))

sys.stdout.write('\n'.join(results) + '\n')


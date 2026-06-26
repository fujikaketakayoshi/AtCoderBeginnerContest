import sys
input = sys.stdin.readline
from itertools import product

N, K, X = map(int, input().split())

Ss = []
for _ in range(N):
    Ss.append(input().strip())

results = []

# product(range(N), repeat=K) で、0〜N-1 の数字から K 個選ぶ全パターンを列挙
# 例: N=3, K=2 なら (0,0), (0,1), (0,2), (1,0)... と生成される
for p in product(range(N), repeat=K):
    current_str = ""
    for i in p:
        current_str += Ss[i]
    results.append(current_str)

# 全ての文字列を辞書順にソート
results.sort()

# X番目（0-indexed なので X-1）を出力
print(results[X - 1])

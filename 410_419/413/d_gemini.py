import sys
input = sys.stdin.readline
from collections import Counter

T = int(input())
out = []

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    # 1. すべて同じ値なら無条件で Yes
    if len(set(A)) == 1:
        out.append("Yes")
        continue
        
    # 要素の出現回数を記録
    count_A = Counter(A)
    
    # 2. 絶対値順にソートして、公比 r の候補を探す
    # 絶対値とその元の値をペアにして、絶対値の昇順でソート
    B = sorted([(abs(x), x) for x in A])
    
    # 最小の絶対値を持つ要素を基準にする
    base = B[0][1]
    
    # 公比 r の候補として、r > 0 の場合と r < 0 の場合を試す
    # B[1][1] / B[0][1] から候補を作る
    # 分数による誤差を避けるため、実数(float)でシミュレーションしつつ、
    # 整数に非常に近いか、あるいは厳密に一致するかで判定する
    
    possible = False
    
    # 基準となる隣り合う2項から公比 r の候補を計算
    # 絶対値が最小の2つの要素から公比を推測する
    r_candidates = []
    
    # B[1][1] を次の項とする場合 (r の候補)
    r1 = B[1][1] / B[0][1]
    r_candidates.append(r1)
    
    # B[1][1] が符号違いの可能性も考慮 (r が負の場合など)
    r2 = -B[1][1] / B[0][1]
    r_candidates.append(r2)
    
    # 重複を排除
    r_candidates = list(set(r_candidates))
    
    for r in r_candidates:
        # base から始めて、公比 r の等比数列を N 項作ってみる
        current = base
        generated = []
        valid_seq = True
        
        for _ in range(N):
            # 整数に丸める（制約が大きいため、誤差対策として round を使用）
            cur_int = round(current)
            if abs(current - cur_int) > 1e-6:
                valid_seq = False
                break
            generated.append(cur_int)
            current *= r
            
        if not valid_seq:
            continue
            
        # 作成した等比数列の要素が、元の A の要素と（個数含めて）一致するか確認
        if Counter(generated) == count_A:
            possible = True
            break
            
    if possible:
        out.append("Yes")
    else:
        out.append("No")
        
print('\n'.join(out))


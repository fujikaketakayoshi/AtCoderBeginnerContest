import sys
input = sys.stdin.readline
from fractions import Fraction

T = int(input())
out = []

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    
    # 1. 要素数が2つの場合は、どんな数でも必ず等比数列になる
    if N == 2:
        out.append("Yes")
        continue
        
    # 2. 絶対値の昇順でソートする
    # 同時に元の符号を保つため、(abs(x), x) のリストにする
    B = sorted([(abs(x), x) for x in A])
    
    # すべての要素の絶対値が同じ場合（例: [2, -2, 2] や [5, 5, 5]）
    if B[0][0] == B[-1][0]:
        # すべて同じ値なら Yes
        if len(set(A)) == 1:
            out.append("Yes")
        # 1 と -1 が混ざっている場合、枚数が同じ（または差が1）で交互に並べられるか
        else:
            # 実際の値を取り出す
            vals = [x[1] for x in B]
            pos_count = sum(1 for x in vals if x > 0)
            neg_count = N - pos_count
            # 差が 1 以内なら交互に並べられる（公比 -1 の等比数列が作れる）
            if abs(pos_count - neg_count) <= 1:
                out.append("Yes")
            else:
                out.append("No")
        continue

    # 3. 隣り合う項の比（公比の絶対値）がすべて等しいかチェック
    # B は絶対値の昇順なので、公比の絶対値は 1 以上になる
    r_abs = Fraction(B[1][0], B[0][0])
    is_geometric_abs = True
    for i in range(1, N - 1):
        if B[1][1] * B[i][1] != B[0][1] * B[i + 1][1]:
        # if Fraction(B[i+1][0], B[i][0]) != r_abs:
            is_geometric_abs = False
            break
            
    if not is_geometric_abs:
        out.append("No")
        continue
        
    # 4. 実際の符号（公比 r の正負）をチェックする
    # 隣り合う項の実際の比（Fraction）を調べる
    r_real = Fraction(B[1][1], B[0][1])
    
    # すべての隣り合う項の比が、r_real または 1/r_real または -r_real などになるか
    # と考えるより、「B を正しく並べ替えたときに一定の比になるか」を判定する。
    # 実は、絶対値ソートした B の段階で、実際の比は「すべて r_real」か「すべて -r_real」のどちらかになるはず。
    
    # 確実なのは、求まった r_real (またはその逆数) を公比として、
    # 「元々の A の正負の個数」と「作られるべき数列の正負の個数」が一致するかチェックすること。
    
    # 公比の絶対値が 1 より大きいので、
    # もし r_real > 0 なら、B の符号はすべて同じ（すべて+、またはすべて-）でなければならない
    # もし r_real < 0 なら、B の符号は交互（+ - + - ... または - + - + ...）でなければならない
    
    is_valid_sign = True
    if r_real > 0:
        # すべての符号が一致しているか
        first_sign = (B[0][1] > 0)
        for i in range(1, N):
            if (B[i][1] > 0) != first_sign:
                is_valid_sign = False
                break
    else:
        # 符号が交互になっているか
        for i in range(1, N):
            if (B[i][1] > 0) == (B[i-1][1] > 0):
                is_valid_sign = False
                break
                
    if is_valid_sign:
        out.append("Yes")
    else:
        # r_real が負の候補だったが、本当は正の公比（の逆数側）だった可能性を考慮
        # 例: A = [-4, -2] から絶対値ソートで B = [(-2, -2), (-4, -4)] となり、r_real = 2 (>0) で上記で判定される。
        # もし符号が噛み合わない場合は No
        out.append("No")

print('\n'.join(out))

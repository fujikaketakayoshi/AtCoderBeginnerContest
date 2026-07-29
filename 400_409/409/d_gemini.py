import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()
    
    if N == 1:
        print(S)
        continue
    
    # 1. S[i] > S[i+1] となる最初の位置(l)を探す
    l = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            l = i
            break
            
    # 2. 最初から辞書順に並んでいるなら、l=r とすれば文字列は変わらないのでそのまま出力
    if l == -1:
        print(S)
        continue

    # 3. l が決まったら、それ以降の j に対して「実際に左シフトした文字列」を比較する
    # target より大きい文字が来たら、それ以降に target を挿入すると
    # その大きい文字が前にズレてきて辞書順が悪化するので break してよい
    target = S[l]
    best_ans = None
    
    for j in range(l, N):
        if S[j] > target:
            break
        
        # l から j までの区間を左シフトした文字列を作成
        current_ans = S[:l] + S[l+1:j+1] + S[l] + S[j+1:]
        
        if best_ans is None or current_ans < best_ans:
            best_ans = current_ans
            
    print(best_ans)
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y, k = map(int, input().split())
    
    xs = [x]
    while x != 0:
        x //= k
        xs.append(x)
        
    ys = [y]
    while y != 0:
        y //= k
        ys.append(y)
    
    l = 0
    r = 0
    
    # xs[l] と ys[r] が一致するまでループ
    while xs[l] != ys[r]:
        # 末尾（根）までの残りの長さ（深さ）を比べる
        # 残りが多い（＝より深いところにいる）方のポインタを進める
        if (len(xs) - l) > (len(ys) - r):
            l += 1
        else:
            r += 1
            
    print(l + r)
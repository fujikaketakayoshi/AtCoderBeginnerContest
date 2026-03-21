import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, H = map(int, input().split())
    
    cur_low = H
    cur_high = H
    prev_t = 0
    
    ok = True
    
    for i in range(N):
        t, l, u = map(int, input().split())
        
        if ok:
            diff = t - prev_t
            new_low = max(0, cur_low - diff)
            new_high = cur_high + diff
            
            inter_low = max(new_low, l)
            inter_high = min(new_high, u)
            
            if inter_low > inter_high:
                ok = False
            else:
                cur_low = inter_low
                cur_high = inter_high
                prev_t = t
    
    print("Yes" if ok else "No")
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    deers = []
    totalP = 0
    
    for _ in range(N):
        W, P = map(int, input().split())
        totalP += P
        deers.append(W + P)
    
    deers.sort()
    print(deers)
    
    s = 0
    ans = 0
    
    for cost in deers:
        if s + cost <= totalP:
            s += cost
            ans += 1
        else:
            break
    
    print(ans)
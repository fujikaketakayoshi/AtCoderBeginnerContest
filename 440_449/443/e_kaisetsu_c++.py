import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, C = map(int, input().split())
    C -= 1  # 0-indexed
    grid = []
    
    for _ in range(N):
        grid.append(input().strip())
    
    # 各列について、最も下にある壁の行番号を記録
    low = [-1] * N
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                low[j] = i
    
    # dpを初期化：スタート列は全行True
    dp = [[False] * N for _ in range(N)]
    for i in range(N):
        dp[i][C] = True
    
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if dp[i][j]:
                continue
            
            ok = False
            if dp[i + 1][j]:
                ok = True
            if j > 0 and dp[i + 1][j - 1]:
                ok = True
            if j + 1 < N and dp[i + 1][j + 1]:
                ok = True
            
            if ok:
                if grid[i][j] == '.':
                    dp[i][j] = True
                else:
                    if low[j] == i:
                        for k in range(i + 1):
                            dp[k][j] = True
    
    ans = ''.join('1' if dp[0][j] else '0' for j in range(N))
    print(ans)
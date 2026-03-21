import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, C = map(int, input().split())
    grid = []

    for _ in range(N):
        grid.append(list(input().strip()))
    
    # 各列について、壁の位置をスタックで管理（下から順に）
    wall_stack = [[] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if grid[y][x] == '#':
                wall_stack[x].append(y)
    
    dp = [[False] * (N + 2) for _ in range(N)]
    dp[N - 1][C] = True

    for y in range(N - 2, -1, -1):
        for x in range(1, N + 1):
            col = x - 1
            
            can_reach = dp[y + 1][x - 1] or dp[y + 1][x] or dp[y + 1][x + 1]
            
            if grid[y][col] == '.':
                dp[y][x] = can_reach
            elif can_reach and wall_stack[col] and wall_stack[col][-1] == y:
                # この壁が列の最下の壁なら破壊可能
                grid[y][col] = '.'
                wall_stack[col].pop()  # O(1)で削除
                dp[y][x] = True
    
    ans = ''.join('1' if dp[0][x] else '0' for x in range(1, N + 1))
    print(ans)
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, C = map(int, input().split())
    grid = []

    for _ in range(N):
        grid.append(list(input().strip()))
    
    dp = [[False] * (N + 2) for _ in range(N)]
    dp[N - 1][C] = True

    for y in range(N - 2, -1, -1):
        for x in range(1, N + 1):
            if grid[y][x - 1] == '.':
                dp[y][x] = any([dp[y + 1][x - 1], dp[y + 1][x], dp[y + 1][x + 1]])
            elif any([dp[y + 1][x - 1], dp[y + 1][x], dp[y + 1][x + 1]]) and all([grid[i][x - 1] == '.' for i in range(y + 1, N)]):
                grid[y][x - 1] = '.'
                dp[y][x] = True
    ans = ''
    for res in dp[0][1:-1]:
        ans += '1' if res else '0'
    print(ans)

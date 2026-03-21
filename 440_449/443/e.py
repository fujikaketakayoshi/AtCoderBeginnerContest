import sys
input = sys.stdin.readline

T = int(input())

dir = [(-1, -1), (-1, 0), (-1, 1)]

def dfs(y, x):
    if y == 0:
        visited[x] = True
        return
    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        if 0 <= ny <= N - 1 and 0 <= nx <= N - 1:
            if grid[ny][nx] == '#':
                if all([grid[i][nx] == '.' for i in range(ny + 1, N)]):
                    grid[ny][nx] = '.'
                    dfs(ny, nx)
                    grid[ny][nx] = '#'
                else:
                    continue
            else:
                dfs(ny, nx)



for _ in range(T):
    N, C = map(int, input().split())
    grid = []
    visited = [False] * N
    for _ in range(N):
        grid.append(list(input().strip()))
    dfs(N - 1, C - 1)

    result = ''
    for i in visited:
        result += '1' if i else '0'
    print(result)

import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

ans = 0

def dfs(i, pos, cnt):
    global ans
    if i == N:
        ans = max(ans, cnt)
        return

    dist = 2 * L[i]

    for sign in (-1, 1):
        npos = pos + sign * dist
        dfs(i + 1, npos, cnt + (pos * npos < 0))  

dfs(0, 1, 0)
print(ans)

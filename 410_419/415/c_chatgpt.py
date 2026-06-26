import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()

    M = 1 << N

    safe = [True] * M

    for mask in range(1, M):
        safe[mask] = (S[mask - 1] == '0')

    dp = [False] * M
    dp[0] = True

    for mask in range(M):
        if not dp[mask]:
            continue

        for i in range(N):
            if mask & (1 << i):
                continue

            nxt = mask | (1 << i)

            if safe[nxt]:
                dp[nxt] = True

    print("Yes" if dp[M - 1] else "No")

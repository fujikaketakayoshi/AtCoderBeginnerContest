import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    S = input().strip()

    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)

    # dp[t][u]
    dp = [[False] * N for _ in range(2 * K + 1)]

    # 残り0手
    for u in range(N):
        dp[0][u] = (S[u] == 'A')

    for t in range(1, 2 * K + 1):
        turn = (2 * K - t) % 2   # 0: Alice, 1: Bob

        for u in range(N):
            if turn == 0:  # Alice
                dp[t][u] = any(dp[t - 1][v] for v in graph[u])
            else:          # Bob
                dp[t][u] = all(dp[t - 1][v] for v in graph[u])

    print("Alice" if dp[2 * K][0] else "Bob")
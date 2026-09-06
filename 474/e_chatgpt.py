import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    A = []
    diff = []

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        diff.append(a - b)

    # Bで買ったときの節約額が大きい順
    diff.sort(reverse=True)

    base = sum(A)
    min_a = min(A)

    ans = base
    saved = 0

    # k = Bで買う商品の種類数
    for k in range(1, N + 1):
        saved += diff[k - 1]

        # Bをk個買うのに不足するクーポン
        extra = max(0, 2 * k - N)

        cost = base - saved + extra * min_a
        ans = min(ans, cost)

    print(ans)
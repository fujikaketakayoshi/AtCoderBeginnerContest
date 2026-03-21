import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    print(N, W, C)

    M = 2 * W

    # 余りごとのコスト合計
    bucket = [0] * M
    for i in range(N):
        bucket[(i + 1) % M] += C[i]

    print(bucket)
    # 円環対応（2倍にする）
    bucket2 = bucket + bucket

    # 最初の区間
    cur = sum(bucket2[:W])
    ans = cur

    # スライド
    for i in range(W, W + M):
        cur += bucket2[i]
        cur -= bucket2[i - W]
        ans = min(ans, cur)

    print(ans)

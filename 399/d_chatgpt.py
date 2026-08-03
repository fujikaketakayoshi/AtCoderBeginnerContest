import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    # pos[x] = 数字xが登場する2つの位置
    pos = [[] for _ in range(N + 1)]

    for i, x in enumerate(A):
        pos[x].append(i)

    ans = set()

    for i in range(2 * N - 1):
        a = A[i]
        b = A[i + 1]

        # 同じカップル同士の隣接は候補にならない
        if a == b:
            continue

        # aが最初から隣接している場合は条件外
        if pos[a][0] + 1 == pos[a][1]:
            continue

        # bが最初から隣接している場合も条件外
        if pos[b][0] + 1 == pos[b][1]:
            continue

        positions = [
            pos[a][0],
            pos[a][1],
            pos[b][0],
            pos[b][1],
        ]
        positions.sort()

        # 4席が「隣接2席 + 隣接2席」になっているか
        if (
            positions[0] + 1 == positions[1]
            and positions[2] + 1 == positions[3]
        ):
            ans.add((min(a, b), max(a, b)))

    print(len(ans))
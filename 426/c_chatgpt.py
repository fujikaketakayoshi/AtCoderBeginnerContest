import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

cnt = [0] + [1] * N
old = 1

for _ in range(Q):
    X, Y = map(int, input().split())

    ans = 0

    while old <= X:
        ans += cnt[old]
        cnt[Y] += cnt[old]
        cnt[old] = 0
        old += 1

    print(ans)

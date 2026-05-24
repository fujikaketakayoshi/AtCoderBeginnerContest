import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

ans = 0

for bit in range(1 << N):
    pos = 1   # 0.5 を 2 倍して 1
    cnt = 0

    for i in range(N):
        dist = 2 * L[i]

        # i ビット目が 1 なら正方向、0 なら負方向
        if bit & (1 << i):
            npos = pos + dist
        else:
            npos = pos - dist

        # 0 を通り過ぎたか判定
        if pos * npos < 0:
            cnt += 1

        pos = npos

    ans = max(ans, cnt)

print(ans)
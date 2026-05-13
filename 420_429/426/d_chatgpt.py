import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().strip()

    cnt0 = S.count('0')
    cnt1 = N - cnt0

    max0 = 0
    max1 = 0

    cur = 1
    for i in range(1, N):
        if S[i] == S[i - 1]:
            cur += 1
        else:
            if S[i - 1] == '0':
                max0 = max(max0, cur)
            else:
                max1 = max(max1, cur)
            cur = 1

    # 最後の連続区間
    if S[-1] == '0':
        max0 = max(max0, cur)
    else:
        max1 = max(max1, cur)

    ans0 = N + cnt0 - 2 * max0
    ans1 = N + cnt1 - 2 * max1

    print(min(ans0, ans1))
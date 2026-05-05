import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()


def calc(start):
    # start='A'なら A B A B ...
    pos = []

    for i, ch in enumerate(S):
        if ch == start:
            pos.append(i)

    ans = 0
    for k in range(N):
        target = 2 * k
        ans += abs(pos[k] - target)

    return ans


print(min(calc('A'), calc('B')))
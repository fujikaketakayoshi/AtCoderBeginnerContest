import sys
input = sys.stdin.readline

N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(M)]


def solve(fixed):
    """
    fixed を (x,y) の一人と固定したとき、
    もう一人になれる候補を返す。
    """
    cand = None

    for a, b in AB:
        # fixed がこの試合にいるなら制約なし
        if a == fixed or b == fixed:
            continue

        # fixed がいない試合なら、
        # 相方は a または b でなければならない
        if cand is None:
            cand = {a, b}
        else:
            cand &= {a, b}

        if len(cand) == 0:
            break

    if cand is None:
        # fixed が全試合に出ていた
        # 相方は誰でもよい（fixed以外）
        return set(range(1, N + 1)) - {fixed}

    # cand.discard(fixed)
    return cand


a1, b1 = AB[0]

ans = set()

a1s = solve(a1)
print(a1s)
for v in a1s:
    x, y = sorted((a1, v))
    ans.add((x, y))

b1s = solve(b1)
print(b1s)
for v in b1s:
    x, y = sorted((b1, v))
    ans.add((x, y))

print(ans)
print(len(ans))
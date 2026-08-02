import sys
input = sys.stdin.readline

N, M = map(int, input().split())

AB = [tuple(map(int, input().split())) for _ in range(M)]


def solve(fixed):
    # 1回目: fixedが常にいるか確認
    all_exist = True
    for a, b in AB:
        if a != fixed and b != fixed:
            all_exist = False
            break

    if all_exist:
        return set(range(1, N + 1)) - {fixed}

    # 2回目: fixedがいない試合だけ積集合
    cand = None
    for a, b in AB:
        if a == fixed or b == fixed:
            continue

        if cand is None:
            cand = {a, b}
        else:
            cand &= {a, b}

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
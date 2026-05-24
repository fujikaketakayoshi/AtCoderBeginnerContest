import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, a, b = map(int, input().split())
    a -= 1
    b -= 1

    # 条件判定
    if n % 2 == 1 or (a + b) % 2 == 0:
        print("No")
        continue

    s1 = []
    s2 = []

    # 縦方向の削減
    for _ in range(n // 2 - 1):
        s = "R" * (n - 1) + "D" + "L" * (n - 1) + "D"
        if a >= 2:
            s1.append(s)
            a -= 2
        else:
            s2.append(s[::-1])
    print(s1, s2)  # デバッグ用

    # 横方向の削減
    for _ in range(n // 2 - 1):
        s = "DRUR"
        if b >= 2:
            s1.append(s)
            b -= 2
        else:
            s2.append(s[::-1])
    print(s1, s2)  # デバッグ用

    # 最後 2x2
    if (a, b) == (0, 1):
        s1.append("DR")
    else:
        s1.append("RD")
    print(s1, s2)  # デバッグ用

    ans = "".join(s1) + "".join(reversed(s2))

    print("Yes")
    print(ans)
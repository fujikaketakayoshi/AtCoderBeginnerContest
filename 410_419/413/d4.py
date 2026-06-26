import sys
input = sys.stdin.readline
from fractions import Fraction

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    # print(N, A)
    B = []
    for a in A:
        B.append((abs(a), a))
    B.sort()
    # すべての要素の絶対値が同じ場合（例: [2, -2, 2] や [5, 5, 5]）
    if B[0][0] == B[-1][0]:
        # すべて同じ値なら Yes
        if len(set(A)) == 1:
            print("Yes")
        # 1 と -1 が混ざっている場合、枚数が同じ（または差が1）で交互に並べられるか
        else:
            # 実際の値を取り出す
            vals = [x[1] for x in B]
            pos_count = sum(1 for x in vals if x > 0)
            neg_count = N - pos_count
            # 差が 1 以内なら交互に並べられる（公比 -1 の等比数列が作れる）
            if abs(pos_count - neg_count) <= 1:
                print("Yes")
            else:
                print("No")
        continue

    ok = True
    for i in range(N - 1):
        if B[1][1] * B[i][1] != B[0][1] * B[i + 1][1]:
            ok = False
            break
    
    if ok:
        signs = []
        for b in B:
            if b[1] < 0:
                signs.append('-')
            else:
                signs.append('+')
        # print(not(all(s == '-' for s in signs) or all(s == '+' for s in signs)))
        if not(all(s == '-' for s in signs) or all(s == '+' for s in signs)):
            if signs[0] == '-':
                if not(all(signs[i] == '-' for i in range(0, N, 2))) or not(all(signs[i] == '+' for i in range(1, N, 2))):
                    ok = False
            else:
                if not(all(signs[i] == '+' for i in range(0, N, 2))) or not(all(signs[i] == '-' for i in range(1, N, 2))):
                    ok = False
    print('Yes' if ok else 'No')

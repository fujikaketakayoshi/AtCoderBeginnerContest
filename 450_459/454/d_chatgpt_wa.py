import sys
input = sys.stdin.readline

T = int(input())

def check(A, B):
    # ① xの並びが一致するか
    if A.replace('(', '').replace(')', '') != B.replace('(', '').replace(')', ''):
        return False

    # ② 左から：開き括弧が過剰にならないか
    cntA = cntB = 0
    for a, b in zip(A, B):
        if a == '(':
            cntA += 1
        elif a == ')':
            cntA -= 1

        if b == '(':
            cntB += 1
        elif b == ')':
            cntB -= 1

        # Aの方が開きすぎると無理
        if cntA < cntB:
            return False

    # ③ 右から：閉じ括弧が過剰にならないか
    cntA = cntB = 0
    for a, b in zip(A[::-1], B[::-1]):
        if a == ')':
            cntA += 1
        elif a == '(':
            cntA -= 1

        if b == ')':
            cntB += 1
        elif b == '(':
            cntB -= 1

        if cntA < cntB:
            return False

    return True

for _ in range(T):
    A = input().strip()
    B = input().strip()
    print("Yes" if check(A, B) else "No")
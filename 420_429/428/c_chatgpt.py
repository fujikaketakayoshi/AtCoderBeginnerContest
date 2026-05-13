import sys
input = sys.stdin.readline

Q = int(input())

stack = []
balance = 0
min_balance = 0

for _ in range(Q):
    query = input().split()

    if query[0] == '1':
        c = query[1]

        # 今の状態を保存（Undo用）
        stack.append((balance, min_balance))

        if c == '(':
            balance += 1
        else:
            balance -= 1

        min_balance = min(min_balance, balance)

    else:
        # 戻す
        balance, min_balance = stack.pop()

    if balance == 0 and min_balance >= 0:
        print("Yes")
    else:
        print("No")
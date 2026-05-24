import sys

# 高速な入出力
input = sys.stdin.read().split()
T = int(input[0])
results = []

idx = 1
for _ in range(T):
    A = input[idx]
    B = input[idx+1]
    idx += 2
    
    # 標準形に変換する関数
    def get_canonical_form(S):
        stack = []
        for char in S:
            stack.append(char)
            # スタックの末尾が (xx) ならカッコを除去
            while len(stack) >= 4:
                if stack[-4:] == ['(', 'x', 'x', ')']:
                    # (xx) の形を見つけたら、カッコを消して xx だけ残す
                    stack.pop() # ')'
                    stack.pop() # 'x'
                    stack.pop() # 'x'
                    stack.pop() # '('
                    stack.append('x')
                    stack.append('x')
                else:
                    break
        print(stack)  # デバッグ用
        return "".join(stack)

    if get_canonical_form(A) == get_canonical_form(B):
        results.append("Yes")
    else:
        results.append("No")
        
print("\n".join(results) + "\n")


import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))  # 1-indexed

ans = [0] * (N + 1)

# 後ろから処理
for i in range(N, 0, -1):
    if A[i] == i:
        ans[i] = i
    else:
        ans[i] = ans[A[i]]

print(*ans[1:])

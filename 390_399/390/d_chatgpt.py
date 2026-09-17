import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

xors = set()
groups = []

def dfs(i, xor):
    if i == N:
        xors.add(xor)
        return

    # 既存グループへ入れる
    for j in range(len(groups)):
        before = groups[j]

        groups[j] += A[i]
        dfs(i + 1, xor ^ before ^ groups[j])
        groups[j] -= A[i]

    # 新しいグループを作る
    groups.append(A[i])
    dfs(i + 1, xor ^ A[i])
    groups.pop()

dfs(0, 0)

print(len(xors))